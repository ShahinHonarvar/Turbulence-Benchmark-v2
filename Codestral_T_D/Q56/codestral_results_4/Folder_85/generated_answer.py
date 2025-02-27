def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 13):
        sub = s[i:i + 14]
        if len(set(sub)) == 14:
            substrings.append(sub)
    return substrings