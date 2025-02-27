def all_substring_of_size_n(text):
    substrings = []
    for i in range(len(text) - 23):
        substring = text[i:i + 24]
        if len(set(substring)) == 24 and substring not in substrings:
            substrings.append(substring)
    return substrings