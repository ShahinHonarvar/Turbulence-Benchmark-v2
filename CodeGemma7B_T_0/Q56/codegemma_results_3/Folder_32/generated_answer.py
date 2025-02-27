def all_substring_of_size_n(text):
    if len(text) < 71:
        return []
    result = set()
    for i in range(len(text) - 71 + 1):
        result.add(text[i:i + 71])
    return list(result)