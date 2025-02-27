def all_substring_of_size_n(s):
    n = len(s)
    result = []
    for i in range(n - 63):
        sub = s[i:i + 64]
        if len(set(sub)) == 64:
            result.append(sub)
    result = list(set(result))
    if len(result) == 0:
        return []
    else:
        return result