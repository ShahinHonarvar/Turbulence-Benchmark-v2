def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 28):
        substring = s[i:i + 29]
        if len(set(substring)) == 29:
            if substring not in substrings:
                substrings.append(substring)
    return substrings