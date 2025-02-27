def all_substring_of_size_n(s):
    if len(s) < 89:
        return []
    substrings = []
    for i in range(len(s) - 88):
        sub = s[i:i + 89]
        if len(set(sub)) == len(sub):
            substrings.append(sub)
    return substrings