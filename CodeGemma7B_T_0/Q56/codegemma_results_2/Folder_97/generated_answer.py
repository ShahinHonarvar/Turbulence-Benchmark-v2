def all_substring_of_size_n(text):
    if len(text) < 142:
        return []
    result = set()
    for i in range(len(text) - 141):
        substring = text[i:i + 142]
        if len(set(substring)) == 142:
            result.add(substring)
    return list(result)