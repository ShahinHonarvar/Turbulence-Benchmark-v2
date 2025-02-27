def all_substring_of_size_n(text):
    if len(text) < 78:
        return []
    substrings = set()
    for i in range(len(text) - 78 + 1):
        substrings.add(text[i:i + 78])
    return list(substrings)