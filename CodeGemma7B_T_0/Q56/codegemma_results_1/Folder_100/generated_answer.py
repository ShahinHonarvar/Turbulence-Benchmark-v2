def all_substring_of_size_n(text):
    if len(text) < 92:
        return []
    substrings = set()
    for i in range(len(text) - 91):
        substrings.add(text[i:i + 92])
    return list(substrings)