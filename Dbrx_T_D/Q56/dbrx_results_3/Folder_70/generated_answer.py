def all_substring_of_size_n(s):
    result = set()
    n = 12
    if len(s) < n:
        return []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == len(set(substring)):
            result.add(substring)
    return list(result)