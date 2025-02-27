def all_substring_of_size_n(text):
    if len(text) < 75:
        return []
    substrings = set()
    for i in range(len(text) - 74):
        substring = text[i:i + 75]
        if len(set(substring)) == 75:
            substrings.add(substring)
    return list(substrings)