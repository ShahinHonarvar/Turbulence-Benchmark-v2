def all_substring_of_size_n(str):
    if len(str) < 12:
        return []
    result = set()
    for i in range(len(str)):
        for j in range(i + 1, min(i + 12, len(str))):
            result.add(str[i:j])
    return list(result)