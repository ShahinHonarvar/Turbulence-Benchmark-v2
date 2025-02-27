def all_substring_of_size_n(text):
    if len(text) < 10:
        return []
    result = set()
    for i in range(len(text) - 9):
        substring = text[i:i + 10]
        if len(set(substring)) == 10:
            result.add(substring)
    return list(result)