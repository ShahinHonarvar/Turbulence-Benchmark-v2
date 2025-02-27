def all_substring_of_size_n(text):
    if len(text) < 90:
        return []
    substrings = set()
    for i in range(len(text) - 89):
        substrings.add(text[i:i + 90])
    return list(substrings)