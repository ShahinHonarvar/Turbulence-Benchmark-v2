def all_substrings_of_size_n(s):
    if len(s) < 65:
        return []
    n = 65
    substrings = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if len(set(sub)) == n:
            substrings.add(sub)
    return list(substrings)