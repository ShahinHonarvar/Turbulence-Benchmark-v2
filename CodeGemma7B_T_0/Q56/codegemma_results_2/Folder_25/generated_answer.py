def all_substring_of_size_n(text):
    if len(text) < 67:
        return []
    result = set()
    for i in range(len(text) - 66):
        result.add(text[i:i + 67])
    return list(result)