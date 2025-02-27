def all_substring_of_size_n(s):
    substrings = []
    length = len(s)
    for i in range(length - 28):
        sub = s[i:i + 29]
        if len(set(sub)) == 29:
            substrings.append(sub)
    return list(set(substrings))