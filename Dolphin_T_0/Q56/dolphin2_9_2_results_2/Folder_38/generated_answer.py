def all_substring_of_size_n(s):
    n = len(s)
    result = set()
    for i in range(n - 2):
        if len(set(s[i:i + 35])) == 35:
            result.add(s[i:i + 35])
    return list(result)