def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 120):
        subs = s[i:i + 120]
        if len(set(subs)) == 120 and subs not in result:
            result.append(subs)
    return result