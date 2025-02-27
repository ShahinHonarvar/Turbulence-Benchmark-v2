def all_substring_of_size_n(text):
    if len(text) < 47:
        return []
    result = set()
    for i in range(len(text) - 46):
        result.add(text[i:i + 47])
    return list(result)