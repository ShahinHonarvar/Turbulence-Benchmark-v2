def all_substring_of_size_n(s):
    n = len(s)
    if n < 39:
        return []
    substrs = []
    for i in range(n - 38):
        sub = s[i:i + 39]
        if len(set(sub)) == 39:
            substrs.append(sub)
    return list(set(substrs))