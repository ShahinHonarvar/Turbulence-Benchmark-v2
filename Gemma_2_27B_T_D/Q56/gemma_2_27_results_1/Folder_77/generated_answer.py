def all_substring_of_size_n(text):
    substrings = set()
    for i in range(len(text) - 143):
        substring = text[i:i + 144]
        if len(set(substring)) == 144:
            substrings.add(substring)
    return list(substrings)