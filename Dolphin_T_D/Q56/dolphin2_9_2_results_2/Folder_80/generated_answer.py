def all_substring_of_size_n(s):
    n = 31
    result = []
    for i in range(len(s) - n + 1):
        subs = s[i:i + n]
        if len(set(subs)) == n:
            result.append(subs)
    return result