def all_substring_of_size_n(text):
    if len(text) < 124:
        return []
    substrings = set()
    for i in range(len(text) - 123):
        substring = text[i:i + 124]
        if len(set(substring)) == 124:
            substrings.add(substring)
    return list(substrings)