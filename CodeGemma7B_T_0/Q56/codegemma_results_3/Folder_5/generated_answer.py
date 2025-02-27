def all_substring_of_size_n(text):
    if len(text) < 64:
        return []
    all_substrings = set()
    for i in range(len(text) - 63):
        substring = text[i:i + 64]
        if len(set(substring)) == 64:
            all_substrings.add(substring)
    return list(all_substrings)