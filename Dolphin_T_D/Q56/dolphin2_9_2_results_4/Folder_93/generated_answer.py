def all_substring_of_size_n(s):
    size = 54
    result = []
    for i in range(len(s) - size + 1):
        subs = s[i:i + size]
        if len(set(subs)) == size and subs not in result:
            result.append(subs)
    return result