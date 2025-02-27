def all_substring_of_size_n(text):
    if len(text) < 100:
        return []
    substrings = set()
    for i in range(len(text) - 99):
        substring = text[i:i + 100]
        if len(set(substring)) == 100:
            substrings.add(substring)
    return list(substrings)