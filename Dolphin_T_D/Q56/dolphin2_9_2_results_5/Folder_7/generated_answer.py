def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 116):
        sub = s[i:i + 117]
        if len(set(sub)) == len(sub):
            substrings.append(sub)
    return substrings