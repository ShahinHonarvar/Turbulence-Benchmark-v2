def all_substring_of_size_n(s):
    result = []
    n = len(s)
    if n < 38:
        return result
    for i in range(n - 37):
        sub = s[i:i + 38]
        if len(set(sub)) == 38:
            result.append(sub)
    return result