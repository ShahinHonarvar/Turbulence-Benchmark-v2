def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 2):
        if len(set(s[i:i + 33])) == 33:
            substrings.append(s[i:i + 33])
    return substrings