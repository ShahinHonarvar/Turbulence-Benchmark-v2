def all_substring_of_size_n(text):
    if len(text) < 30:
        return []
    result = set()
    for i in range(len(text) - 29):
        substring = text[i:i + 30]
        if len(set(substring)) == 30:
            result.add(substring)
    return list(result)