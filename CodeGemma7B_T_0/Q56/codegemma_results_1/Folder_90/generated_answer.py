def all_substring_of_size_n(text):
    if len(text) < 130:
        return []
    result = set()
    for i in range(len(text) - 129):
        result.add(text[i:i + 130])
    return list(result)