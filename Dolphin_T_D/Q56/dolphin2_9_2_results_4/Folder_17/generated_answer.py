def all_substring_of_size_n(s):
    if len(s) < 37:
        return []
    substrings = set()
    for i in range(0, len(s) - 36):
        sub = s[i:i + 37]
        if len(set(sub)) == 37:
            substrings.add(sub)
    return list(substrings)