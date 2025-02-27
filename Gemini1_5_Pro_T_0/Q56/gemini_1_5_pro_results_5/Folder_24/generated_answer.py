def all_substring_of_size_n(text):
    substrings = []
    for i in range(len(text) - 51 + 1):
        substring = text[i:i + 52]
        if len(set(substring)) == 52:
            if substring not in substrings:
                substrings.append(substring)
    return substrings