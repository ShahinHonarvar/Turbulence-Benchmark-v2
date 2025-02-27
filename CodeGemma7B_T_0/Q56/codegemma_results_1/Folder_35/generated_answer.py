def all_substring_of_size_n(text):
    if len(text) < 27:
        return []
    all_substrings = set()
    for i in range(len(text) - 26):
        substring = text[i:i + 27]
        if len(set(substring)) == 27:
            all_substrings.add(substring)
    return list(all_substrings)