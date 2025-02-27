def all_substring_of_size_n(s):
    n = 11
    substrs = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if len(set(sub)) == n:
            substrs.add(sub)
    return list(substrs)