def all_substring_of_size_n(text):
    if len(text) < 94:
        return []
    substrings = set()
    for i in range(len(text) - 93):
        substrings.add(text[i:i + 94])
    return list(substrings)