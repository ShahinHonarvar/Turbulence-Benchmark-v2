def all_substring_of_size_n(text):
    if len(text) < 53:
        return []
    result = set()
    for i in range(len(text) - 52):
        result.add(text[i:i + 53])
    return list(result)