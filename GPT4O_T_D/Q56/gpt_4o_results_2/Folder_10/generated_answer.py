def all_substring_of_size_n(s):
    results = []
    n = 55
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if len(substr) == n and len(set(substr)) == n:
            results.append(substr)
    return results