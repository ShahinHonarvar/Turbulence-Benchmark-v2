def all_substring_of_size_n(text):
    substrings = []
    if len(text) >= 84:
        for i in range(len(text) - 83):
            substring = text[i:i + 84]
            if len(set(substring)) == 84:
                substrings.append(substring)
    return substrings