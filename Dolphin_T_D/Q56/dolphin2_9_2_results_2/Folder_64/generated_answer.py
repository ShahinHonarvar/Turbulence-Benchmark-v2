def all_substring_of_size_n(s):
    if len(s) < 8:
        return []
    substrs = set()
    for i in range(len(s) - 7):
        sub = s[i:i + 8]
        if len(set(sub)) == 8:
            substrs.add(sub)
    return list(substrs)