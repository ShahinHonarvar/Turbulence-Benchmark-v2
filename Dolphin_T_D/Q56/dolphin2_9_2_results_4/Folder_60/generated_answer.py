def all_substring_of_size_n(s):
    substrings = set()
    n = len(s)
    if n < 36:
        return []
    for i in range(n - 35):
        sub = s[i:i + 36]
        if len(set(sub)) == 36:
            substrings.add(sub)
    return list(substrings)