def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 40 + 1):
        if len(set(s[i:i + 40])) == 40:
            substrings.append(s[i:i + 40])
    return substrings