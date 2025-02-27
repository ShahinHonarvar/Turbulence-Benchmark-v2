def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 96):
        sub = s[i:i + 97]
        if len(set(sub)) == 97:
            substrings.append(sub)
    return substrings