def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 7):
        if len(set(s[i:i + 8])) == 8:
            substrings.append(s[i:i + 8])
    return list(set(substrings))