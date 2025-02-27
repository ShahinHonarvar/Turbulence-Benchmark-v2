def all_substring_of_size_n(text):
    if len(text) < 81:
        return []
    result = set()
    for i in range(len(text) - 80):
        result.add(text[i:i + 81])
    return list(result)