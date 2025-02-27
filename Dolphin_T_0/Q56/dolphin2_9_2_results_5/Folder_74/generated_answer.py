def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 96):
        if len(set(s[i:i + 97])) == 97:
            substrings.append(s[i:i + 97])
    return substrings