def all_substring_of_size_n(s):
    n = 142
    substrs = []
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if len(set(sub)) == n:
            substrs.append(sub)
    return list(set(substrs))