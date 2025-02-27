def all_substring_of_size_n(text):
    if len(text) < 146:
        return []
    substrings = set()
    for i in range(len(text) - 145):
        substring = text[i:i + 146]
        if len(set(substring)) == 146:
            substrings.add(substring)
    return list(substrings)