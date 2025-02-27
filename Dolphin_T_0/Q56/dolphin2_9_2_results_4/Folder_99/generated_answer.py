def all_substring_of_size_n(s):
    if len(set(s)) < 110:
        return []
    substrings = set()
    for i in range(len(s) - 110):
        sub = s[i:i + 110]
        if len(set(sub)) == len(sub):
            substrings.add(sub)
    return list(substrings)