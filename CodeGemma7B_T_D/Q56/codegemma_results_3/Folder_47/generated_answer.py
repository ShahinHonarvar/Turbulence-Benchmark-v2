def all_substring_of_size_n(s):
    if len(s) < 91:
        return []
    result = set()
    for start in range(len(s) - 90):
        substring = s[start:start + 91]
        result.add(substring)
    return list(result)