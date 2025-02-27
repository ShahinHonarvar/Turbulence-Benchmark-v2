def all_substring_of_size_n(text):
    if len(text) < 16:
        return []
    result = set()
    for i in range(len(text) - 15):
        result.add(text[i:i + 16])
    return list(result)