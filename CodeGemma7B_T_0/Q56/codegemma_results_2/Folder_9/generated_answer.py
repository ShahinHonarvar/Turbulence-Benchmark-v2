def all_substring_of_size_n(text):
    if len(text) < 34:
        return []
    result = set()
    for i in range(len(text) - 33):
        result.add(text[i:i + 34])
    return list(result)