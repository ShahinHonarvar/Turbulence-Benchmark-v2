def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 29:
        return substrings
    for i in range(len(s) - 28):
        substring = s[i:i + 29]
        if len(set(substring)) == 29:
            substrings.append(substring)
    return substrings