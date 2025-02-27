def all_substring_of_size_n(text):
    if len(text) < 26:
        return []
    all_substrings = set()
    for i in range(len(text) - 25):
        substring = text[i:i + 26]
        if len(set(substring)) == 26:
            all_substrings.add(substring)
    return list(all_substrings)