def all_substring_of_size_n(text):
    if len(text) < 36:
        return []
    result = set()
    for i in range(len(text) - 35):
        substring = text[i:i + 36]
        if len(set(substring)) == 36:
            result.add(substring)
    return list(result)