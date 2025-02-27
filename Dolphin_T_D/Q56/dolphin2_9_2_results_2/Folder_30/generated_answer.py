def all_substring_of_size_n(s):
    n = len(s)
    substrings = []
    for i in range(0, n - 78):
        sub = s[i:i + 79]
        if len(set(sub)) == len(sub):
            substrings.append(sub)
    return substrings