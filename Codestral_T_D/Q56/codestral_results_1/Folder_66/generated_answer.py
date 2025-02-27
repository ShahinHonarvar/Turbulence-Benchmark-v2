def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 25):
        sub = s[i:i + 26]
        if len(set(sub)) == 26:
            substrings.append(sub)
    return substrings