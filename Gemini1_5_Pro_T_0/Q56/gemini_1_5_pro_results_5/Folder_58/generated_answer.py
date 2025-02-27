def all_substring_of_size_n(text):
    substrings = []
    for i in range(len(text) - 127 + 1):
        substring = text[i:i + 127]
        if len(set(substring)) == 127 and substring not in substrings:
            substrings.append(substring)
    return substrings