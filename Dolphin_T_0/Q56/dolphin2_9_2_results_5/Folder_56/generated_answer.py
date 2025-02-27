def all_substring_of_size_n(s):
    n = len(s)
    substrings = []
    for i in range(n - 68):
        sub = s[i:i + 69]
        if len(set(sub)) == 69:
            substrings.append(sub)
    return substrings