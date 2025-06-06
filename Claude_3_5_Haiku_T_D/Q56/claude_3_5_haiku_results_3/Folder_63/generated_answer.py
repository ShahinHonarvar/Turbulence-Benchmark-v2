def all_substring_of_size_n(s):
    n = 19
    result = set()
    if len(s) < n:
        return list(result)
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            result.add(substring)
    return list(result)