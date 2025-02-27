def all_substring_of_size_n(text):
    substrings = []
    for i in range(len(text) - 74):
        substring = text[i:i + 75]
        if len(set(substring)) == 75 and substring not in substrings:
            substrings.append(substring)
    return substrings