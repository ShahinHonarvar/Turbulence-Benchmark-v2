def all_substring_of_size_n(text):
    if len(text) < 45:
        return []
    substrings = set()
    for i in range(len(text) - 44):
        substring = text[i:i + 45]
        if len(set(substring)) == 45:
            substrings.add(substring)
    return list(substrings)