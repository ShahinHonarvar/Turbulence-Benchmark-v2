def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 148):
        sub = s[i:i + 149]
        if len(sub) == len(set(sub)) == 149:
            substrings.append(sub)
    return substrings