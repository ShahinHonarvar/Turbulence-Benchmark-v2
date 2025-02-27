def all_substring_of_size_n(str):
    if len(str) < 58:
        return []
    result = set()
    for i in range(len(str) - 58 + 1):
        result.add(str[i:i + 58])
    return list(result)