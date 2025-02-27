def all_substring_of_size_n(s):
    n = 84
    substrings = []
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if len(set(sub)) == n:
            substrings.append(sub)
    return substrings