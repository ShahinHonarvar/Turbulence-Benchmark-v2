def all_substring_of_size_n(text):
    if len(text) < 69:
        return []
    substrings = set()
    for i in range(len(text) - 68):
        substrings.add(text[i:i + 69])
    return list(substrings)