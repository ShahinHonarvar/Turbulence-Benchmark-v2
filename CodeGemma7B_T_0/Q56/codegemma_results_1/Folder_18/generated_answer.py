def all_substring_of_size_n(text):
    if len(text) < 63:
        return []
    result = set()
    for i in range(len(text) - 62):
        result.add(text[i:i + 63])
    return list(result)