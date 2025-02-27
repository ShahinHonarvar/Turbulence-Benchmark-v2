def all_substring_of_size_n(text):
    substrings = []
    for i in range(len(text) - 44):
        substring = text[i:i + 45]
        if len(set(substring)) == 45 and substring not in substrings:
            substrings.append(substring)
    return substrings