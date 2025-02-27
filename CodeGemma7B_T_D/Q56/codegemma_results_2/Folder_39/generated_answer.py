def all_substring_of_size_n(s):
    if len(s) < 94:
        return []
    result = set()
    for i in range(len(s) - 93):
        result.add(s[i:i + 94])
    return list(result)