def all_substring_of_size_n(text):
    if len(text) < 144:
        return []
    all_substrings = set()
    for i in range(len(text) - 143):
        substring = text[i:i + 144]
        if len(set(substring)) == 144:
            all_substrings.add(substring)
    return list(all_substrings)