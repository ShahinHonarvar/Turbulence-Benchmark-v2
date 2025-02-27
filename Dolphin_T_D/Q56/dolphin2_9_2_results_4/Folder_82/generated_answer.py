def all_substring_of_size_n(s):
    result = []
    for i in range(100, len(s) + 1):
        subs = s[i - 100:i]
        if len(set(subs)) == 100:
            result.append(subs)
    return result