def all_substring_of_size_n(s):
    substrings = set()
    n = len(s)
    for i in range(n - 26 + 1):
        sub = s[i:i + 26]
        if len(set(sub)) == 26:
            substrings.add(sub)
    return list(substrings)