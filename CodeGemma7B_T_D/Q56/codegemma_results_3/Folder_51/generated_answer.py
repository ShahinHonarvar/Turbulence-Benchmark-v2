def all_substring_of_size_n(str):
    result = set()
    for i in range(len(str) - 96 + 1):
        result.add(str[i:i + 96])
    return list(result)