def all_substring_of_size_n(text):
    if len(text) < 48:
        return []
    all_substrings = set()
    for i in range(len(text) - 48 + 1):
        substring = text[i:i + 48]
        if len(set(substring)) == 48:
            all_substrings.add(substring)
    return list(all_substrings)