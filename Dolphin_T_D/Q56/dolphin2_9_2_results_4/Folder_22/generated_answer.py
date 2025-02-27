def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 21):
        sub = s[i:i + 22]
        if len(set(sub)) == 22:
            substrings.append(sub)
    return substrings