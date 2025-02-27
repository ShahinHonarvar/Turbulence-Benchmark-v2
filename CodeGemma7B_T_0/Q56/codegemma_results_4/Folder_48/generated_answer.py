def all_substring_of_size_n(text):
    if len(text) < 120:
        return []
    result = set()
    for i in range(len(text) - 119):
        result.add(text[i:i + 120])
    return list(result)