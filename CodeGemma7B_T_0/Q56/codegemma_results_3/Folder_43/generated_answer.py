def all_substring_of_size_n(text):
    if len(text) < 86:
        return []
    result = set()
    for i in range(len(text) - 85):
        result.add(text[i:i + 86])
    return list(result)