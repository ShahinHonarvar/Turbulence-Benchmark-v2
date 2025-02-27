def all_substring_of_size_n(s):
    n = 12
    substrings = []
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if len(set(list(sub))) == n:
            substrings.append(sub)
    return substrings