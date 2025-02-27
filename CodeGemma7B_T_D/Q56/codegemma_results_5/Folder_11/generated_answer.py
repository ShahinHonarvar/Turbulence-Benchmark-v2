def all_substring_of_size_n(s):
    if len(s) < 78:
        return []
    result = set()
    for i in range(len(s) - 78 + 1):
        substring = s[i:i + 78]
        result.add(substring)
    return list(result)