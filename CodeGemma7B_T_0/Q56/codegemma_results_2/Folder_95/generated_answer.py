def all_substring_of_size_n(text):
    if len(text) < 89:
        return []
    result = set()
    for i in range(len(text) - 88):
        result.add(text[i:i + 89])
    return list(result)