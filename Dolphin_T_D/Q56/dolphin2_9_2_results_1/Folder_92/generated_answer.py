def all_substring_of_size_n(s):
    if len(s) < 9:
        return []
    n = len(s)
    substrings = set()
    for i in range(n - 8):
        sub = s[i:i + 9]
        if len(set(sub)) == 9:
            substrings.add(sub)
    return list(substrings)