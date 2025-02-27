def all_substring_of_size_n(text):
    if len(text) < 105:
        return []
    all_substrings = set()
    for i in range(len(text) - 105 + 1):
        substring = text[i:i + 105]
        if len(set(substring)) == 105:
            all_substrings.add(substring)
    return list(all_substrings)