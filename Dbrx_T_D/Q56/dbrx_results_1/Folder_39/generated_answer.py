def all_substring_of_size_n(s):
    result = set()
    n = 94
    if len(s) < n:
        return []
    for i in range(len(s) - n + 1):
        substring = ''.join(sorted(s[i:i + n]))
        result.add(substring)
    return list(result)