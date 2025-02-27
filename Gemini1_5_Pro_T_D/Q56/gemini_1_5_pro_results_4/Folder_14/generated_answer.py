def all_substring_of_size_n(text):
    substrings = []
    for i in range(len(text) - 84):
        substring = text[i:i + 85]
        if len(set(substring)) == 85 and substring not in substrings:
            substrings.append(substring)
    return substrings