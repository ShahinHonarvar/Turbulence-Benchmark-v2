def all_substring_of_size_n(s):
    if len(s) < 60:
        return []
    result = set()
    for i in range(len(s) - 59):
        result.add(s[i:i + 60])
    return list(result)