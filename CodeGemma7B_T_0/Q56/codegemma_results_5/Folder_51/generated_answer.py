def all_substring_of_size_n(str):
    if len(str) < 96:
        return []
    result = set()
    for i in range(len(str) - 95):
        result.add(str[i:i + 96])
    return list(result)