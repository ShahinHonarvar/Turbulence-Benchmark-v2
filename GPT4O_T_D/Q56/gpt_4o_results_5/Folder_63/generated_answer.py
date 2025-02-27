def all_substring_of_size_n(s):
    substrings = set()
    n = len(s)
    for i in range(n - 18):
        sub = s[i:i + 19]
        if len(sub) == 19 and len(set(sub)) == 19:
            substrings.add(sub)
    return list(substrings)