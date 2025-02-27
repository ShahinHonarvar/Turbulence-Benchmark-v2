def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 93):
        if len(set(s[i:i + 94])) == 94:
            substrings.append(s[i:i + 94])
    return substrings