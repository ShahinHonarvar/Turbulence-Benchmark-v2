def all_substring_of_size_n(text):
    if len(text) < 33:
        return []
    result = set()
    for i in range(len(text) - 32):
        substring = text[i:i + 33]
        if len(set(substring)) == 33:
            result.add(substring)
    return list(result)