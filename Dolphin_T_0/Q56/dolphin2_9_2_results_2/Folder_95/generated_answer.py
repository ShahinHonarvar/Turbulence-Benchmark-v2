def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 88):
        if len(set(s[i:i + 89])) == 89:
            substrings.append(s[i:i + 89])
    return substrings