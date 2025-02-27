def all_substring_of_size_n(text):
    if len(text) < 39:
        return []
    result = set()
    for i in range(len(text) - 38):
        substring = text[i:i + 39]
        if len(set(substring)) == 39:
            result.add(substring)
    return list(result)