def all_substring_of_size_n(text):
    substrings = []
    if len(text) < 94:
        return substrings
    for i in range(len(text) - 93):
        substring = text[i:i + 94]
        if len(set(substring)) == 94:
            substrings.append(substring)
    return substrings