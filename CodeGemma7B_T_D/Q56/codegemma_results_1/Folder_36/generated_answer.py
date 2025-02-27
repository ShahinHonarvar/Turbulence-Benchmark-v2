def all_substring_of_size_n(text):
    substrings = []
    for i in range(len(text) - 146 + 1):
        substring = text[i:i + 146]
        if len(set(substring)) == 146:
            substrings.append(substring)
    return substrings