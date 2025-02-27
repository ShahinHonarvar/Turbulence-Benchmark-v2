def all_substring_of_size_n(text):
    if len(text) < 84:
        return []
    all_substrings = set()
    for i in range(len(text) - 83):
        substring = text[i:i + 84]
        if len(set(substring)) == 84:
            all_substrings.add(substring)
    return list(all_substrings)