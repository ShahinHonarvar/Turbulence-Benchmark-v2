def all_substring_of_size_n(str):
    if len(str) < 54:
        return []
    result = set()
    for i in range(len(str) - 53):
        result.add(str[i:i + 54])
    return list(result)