def all_substring_of_size_n(s):
    substrings = set()
    n = 146
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if len(set(sub)) == n:
            substrings.add(sub)
    if len(substrings) == 0:
        return []
    else:
        return list(substrings)