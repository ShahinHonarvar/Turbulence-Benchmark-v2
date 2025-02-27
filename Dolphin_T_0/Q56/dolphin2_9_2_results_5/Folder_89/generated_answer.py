def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 37):
        sub = s[i:i + 38]
        if len(set(sub)) == len(sub) and len(sub) == 38:
            substrings.append(sub)
    return substrings