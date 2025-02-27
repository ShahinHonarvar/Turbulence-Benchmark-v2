def all_substring_of_size_n(text):
    if len(text) < 35:
        return []
    result = set()
    for i in range(len(text) - 34):
        result.add(text[i:i + 35])
    return list(result)