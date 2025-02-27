def all_substring_of_size_n(str):
    if len(str) < 24:
        return []
    result = set()
    for i in range(len(str) - 23):
        result.add(str[i:i + 24])
    return list(result)