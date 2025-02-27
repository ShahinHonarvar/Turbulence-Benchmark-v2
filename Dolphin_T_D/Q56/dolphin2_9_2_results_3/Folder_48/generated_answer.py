def all_substring_of_size_n(s):
    if len(s) < 120:
        return []
    n = len(s)
    result = set()
    for i in range(n - 120 + 1):
        sub = s[i:i + 120]
        if len(set(sub)) == len(sub):
            result.add(sub)
    return list(result)