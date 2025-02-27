def all_substring_of_size_n(text):
    if len(text) < 79:
        return []
    substrings = set()
    for i in range(len(text) - 78):
        substrings.add(text[i:i + 79])
    return list(substrings)