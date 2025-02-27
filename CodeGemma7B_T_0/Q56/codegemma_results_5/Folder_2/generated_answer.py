def all_substring_of_size_n(text):
    if len(text) < 56:
        return []
    result = set()
    for i in range(len(text) - 55):
        substring = text[i:i + 56]
        if len(set(substring)) == 56:
            result.add(substring)
    return list(result)