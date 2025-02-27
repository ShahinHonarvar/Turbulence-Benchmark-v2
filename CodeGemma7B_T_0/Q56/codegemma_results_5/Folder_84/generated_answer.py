def all_substring_of_size_n(text):
    if len(text) < 114:
        return []
    all_substrings = set()
    for i in range(len(text) - 113):
        substring = text[i:i + 114]
        if len(set(substring)) == 114:
            all_substrings.add(substring)
    return list(all_substrings)