def all_substring_of_size_n(s):
    substrings = []
    n = len(s)
    for i in range(n - 27):
        sub = s[i:i + 28]
        if len(set(sub)) == 28:
            substrings.append(sub)
    return substrings