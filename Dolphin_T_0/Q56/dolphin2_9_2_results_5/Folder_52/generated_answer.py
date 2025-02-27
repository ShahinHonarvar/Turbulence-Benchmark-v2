def all_substring_of_size_n(s):
    substrings = set()
    n = 15
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        duplicates = [sub.count(c) > 1 for c in sub]
        if not any(duplicates):
            substrings.add(sub)
    return list(substrings)