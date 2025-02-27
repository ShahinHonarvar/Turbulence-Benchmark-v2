def all_substring_of_size_n(str):
    result = set()
    for i in range(len(str) - 98 + 1):
        result.add(str[i:i + 98])
    return list(result)