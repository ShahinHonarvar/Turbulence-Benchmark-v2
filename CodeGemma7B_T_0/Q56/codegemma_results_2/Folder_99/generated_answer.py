def all_substring_of_size_n(text):
    if len(text) < 110:
        return []
    result = set()
    for i in range(len(text) - 110 + 1):
        substring = text[i:i + 110]
        if len(set(substring)) == 110:
            result.add(substring)
    return list(result)