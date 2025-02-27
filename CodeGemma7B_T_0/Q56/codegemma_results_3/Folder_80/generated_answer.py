def all_substring_of_size_n(text):
    if len(text) < 31:
        return []
    result = set()
    for i in range(len(text) - 30):
        result.add(text[i:i + 31])
    return list(result)