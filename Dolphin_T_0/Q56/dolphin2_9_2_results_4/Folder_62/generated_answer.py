def all_substring_of_size_n(s):
    n = 32
    if len(s) < n:
        return []
    substrings = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if len(sub) == len(set(sub)):
            substrings.add(sub)
    return list(substrings)