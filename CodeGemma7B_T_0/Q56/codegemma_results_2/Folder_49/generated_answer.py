def all_substring_of_size_n(text):
    if len(text) < 73:
        return []
    substrings = set()
    for i in range(len(text) - 72):
        substring = text[i:i + 73]
        if len(set(substring)) == 73:
            substrings.add(substring)
    return list(substrings)