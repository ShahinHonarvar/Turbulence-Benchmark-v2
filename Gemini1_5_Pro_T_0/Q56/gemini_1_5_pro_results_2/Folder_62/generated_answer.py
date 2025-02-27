def all_substring_of_size_n(text):
    substrings = []
    for i in range(len(text) - 32 + 1):
        substring = text[i:i + 32]
        if len(set(substring)) == 32:
            substrings.append(substring)
    return list(set(substrings))