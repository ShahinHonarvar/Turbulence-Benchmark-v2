def all_substring_of_size_n(s):
    n = len(s)
    substrings = []
    for i in range(n - 142):
        sub = s[i:i + 143]
        if len(set(sub)) == len(sub):
            substrings.append(sub)
    return substrings