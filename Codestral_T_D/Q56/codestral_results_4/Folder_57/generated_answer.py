def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 60 + 1):
        sub = s[i:i + 60]
        if len(set(sub)) == 60:
            substrings.append(sub)
    return substrings