def all_substring_of_size_n(text):
    if len(text) < 14:
        return []
    result = set()
    for i in range(len(text) - 13):
        result.add(text[i:i + 14])
    return list(result)