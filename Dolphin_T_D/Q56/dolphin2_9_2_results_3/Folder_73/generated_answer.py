def all_substring_of_size_n(s):
    n = 20
    substrings = []
    length = len(s)
    if length < n:
        return substrings
    for i in range(length - n + 1):
        sub = s[i:i + n]
        if len(set(sub)) == n:
            substrings.append(sub)
    return substrings