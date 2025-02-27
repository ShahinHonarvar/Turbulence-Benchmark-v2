def all_substring_of_size_n(text):
    if len(text) < 57:
        return []
    substrings = set()
    for i in range(len(text) - 56):
        substrings.add(text[i:i + 57])
    return list(substrings)