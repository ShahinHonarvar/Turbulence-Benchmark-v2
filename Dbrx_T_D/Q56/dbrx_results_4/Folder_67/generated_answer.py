def all_substring_of_size_n(s):
    result = set()
    if len(s) < 43:
        return []
    for i in range(len(s) - 42):
        substring = ''.join(sorted(s[i:i + 43]))
        result.add(substring)
    return list(result)