def all_substring_of_size_n(str):
    if len(str) < 52:
        return []
    result = set()
    for i in range(len(str) - 51):
        result.add(str[i:i + 52])
    return list(result)