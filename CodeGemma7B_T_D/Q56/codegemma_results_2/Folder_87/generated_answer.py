def all_substring_of_size_n(str):
    if len(str) < 58:
        return []
    result = set()
    for i in range(len(str)):
        for j in range(i + 58, len(str) + 1):
            substring = str[i:j]
            if len(substring) == 58:
                result.add(substring)
    return list(result)