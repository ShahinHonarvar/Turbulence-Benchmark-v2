def all_substring_of_size_n(text):
    if len(text) < 127:
        return []
    result = set()
    for i in range(len(text) - 127 + 1):
        substring = text[i:i + 127]
        if len(set(substring)) == 127:
            result.add(substring)
    return list(result)