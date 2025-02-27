def all_substring_of_size_n(text):
    substrings = []
    for i in range(len(text) - 145):
        substring = text[i:i + 146]
        if len(set(substring)) == 146 and substring not in substrings:
            substrings.append(substring)
    return substrings