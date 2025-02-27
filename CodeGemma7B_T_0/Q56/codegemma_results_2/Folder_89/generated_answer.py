def all_substring_of_size_n(text):
    if len(text) < 38:
        return []
    result = set()
    for i in range(len(text) - 38 + 1):
        result.add(text[i:i + 38])
    return list(result)