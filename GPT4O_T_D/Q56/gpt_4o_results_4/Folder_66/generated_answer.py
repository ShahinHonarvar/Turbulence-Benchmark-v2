def all_substring_of_size_n(s):
    result = []
    n = len(s)
    if n < 26:
        return result
    for i in range(n - 25):
        sub = s[i:i + 26]
        if len(set(sub)) == 26:
            result.append(sub)
    return result