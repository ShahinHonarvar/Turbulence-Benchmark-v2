def all_substring_of_size_n(s):
    if len(s) < 8:
        return []
    i = 0
    n = len(s)
    substrings = set()
    while i + 7 < n:
        sub = s[i:i + 8]
        if len(set(sub)) == 8:
            substrings.add(sub)
        i += 1
    return list(substrings)