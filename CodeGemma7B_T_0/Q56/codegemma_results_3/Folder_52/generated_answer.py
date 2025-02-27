def all_substring_of_size_n(text):
    if len(text) < 15:
        return []
    result = set()
    for i in range(len(text) - 14):
        result.add(text[i:i + 15])
    return list(result)