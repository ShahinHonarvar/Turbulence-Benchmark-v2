def all_substring_of_size_n(text):
    if len(text) < 117:
        return []
    all_substrings = set()
    for i in range(len(text) - 116):
        substring = text[i:i + 117]
        if len(set(substring)) == 117:
            all_substrings.add(substring)
    return list(all_substrings)