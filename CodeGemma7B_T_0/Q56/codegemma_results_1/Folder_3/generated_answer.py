def all_substring_of_size_n(text):
    if len(text) < 93:
        return []
    result = set()
    for i in range(len(text) - 92):
        substring = text[i:i + 93]
        if len(set(substring)) == 93:
            result.add(substring)
    return list(result)