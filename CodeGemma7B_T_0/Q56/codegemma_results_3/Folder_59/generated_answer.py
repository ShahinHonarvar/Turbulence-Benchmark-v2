def all_substring_of_size_n(text):
    if len(text) < 77:
        return []
    result = set()
    for i in range(len(text) - 76):
        result.add(text[i:i + 77])
    return list(result)