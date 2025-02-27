def all_substring_of_size_n(s):
    result = set()
    n = 63
    if len(s) < n:
        return []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == n and len(set(substring)) == n:
            result.add(substring)
    return list(result)