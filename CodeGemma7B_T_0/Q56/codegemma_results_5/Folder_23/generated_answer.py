def all_substring_of_size_n(text):
    if len(text) < 42:
        return []
    all_substrings = set()
    for i in range(len(text) - 41):
        substring = text[i:i + 42]
        if len(set(substring)) == 42:
            all_substrings.add(substring)
    return list(all_substrings)