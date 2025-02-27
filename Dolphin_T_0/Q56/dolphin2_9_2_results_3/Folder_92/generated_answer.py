def all_substring_of_size_n(s):
    result = set()
    n = len(s)
    for i in range(n - 8):
        sub = s[i:i + 9]
        if len(set(sub)) == 9:
            result.add(sub)
    return list(result)