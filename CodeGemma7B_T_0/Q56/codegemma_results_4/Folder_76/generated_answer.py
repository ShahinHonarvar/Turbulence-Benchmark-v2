def all_substring_of_size_n(text):
    if len(text) < 149:
        return []
    all_substrings = set()
    for i in range(len(text) - 148):
        substring = text[i:i + 149]
        if len(set(substring)) == 149:
            all_substrings.add(substring)
    return list(all_substrings)