def all_substring_of_size_n(str):
    if len(str) < 106:
        return []
    result = set()
    for i in range(len(str) - 105):
        substring = str[i:i + 106]
        if len(set(substring)) == 106:
            result.add(substring)
    return list(result)