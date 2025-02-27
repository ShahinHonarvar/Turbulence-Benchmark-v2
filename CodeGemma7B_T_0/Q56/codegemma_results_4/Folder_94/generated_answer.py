def all_substring_of_size_n(text):
    if len(text) < 70:
        return []
    substrings = set()
    for i in range(len(text) - 69):
        substrings.add(text[i:i + 70])
    return list(substrings)