def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 9):
        sub = s[i:i + 10]
        if len(set(sub)) == 10:
            substrings.append(sub)
    return substrings