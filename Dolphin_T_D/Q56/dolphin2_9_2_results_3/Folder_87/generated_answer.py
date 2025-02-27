def all_substring_of_size_n(s):
    n = len(s)
    result = set()
    if n < 58:
        return []
    for i in range(n - 57):
        sub = s[i:i + 58]
        if len(set(sub)) == 58:
            result.add(sub)
    return list(result)