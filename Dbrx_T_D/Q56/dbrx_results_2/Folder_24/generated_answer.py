def all_substring_of_size_n(s):
    result = set()
    n = 52
    if len(s) < n:
        return []
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if len(substr) == len(set(substr)):
            result.add(substr)
    return list(result)