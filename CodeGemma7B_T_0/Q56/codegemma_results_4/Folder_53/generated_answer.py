def all_substring_of_size_n(text):
    if len(text) < 25:
        return []
    result = set()
    for i in range(len(text) - 24):
        result.add(text[i:i + 25])
    return list(result)