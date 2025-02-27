def all_substring_of_size_n(s):
    if len(s) < 41:
        return []
    result = set()
    for i in range(len(s) - 40):
        substring = s[i:i + 41]
        result.add(substring)
    return list(result)