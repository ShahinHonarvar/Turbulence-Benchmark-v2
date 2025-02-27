def all_substring_of_size_n(text):
    if len(text) < 91:
        return []
    all_substrings = set()
    for i in range(len(text) - 90):
        substring = text[i:i + 91]
        if len(set(substring)) == 91:
            all_substrings.add(substring)
    return list(all_substrings)