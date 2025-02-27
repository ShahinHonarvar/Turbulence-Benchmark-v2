def all_substring_of_size_n(text):
    if len(text) < 68:
        return []
    all_substrings = set()
    for i in range(len(text) - 68 + 1):
        substring = text[i:i + 68]
        if len(set(substring)) == 68:
            all_substrings.add(substring)
    return list(all_substrings)