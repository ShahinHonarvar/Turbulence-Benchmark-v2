def all_substring_of_size_n(s):
    substrs = set()
    n = len(s)
    for i in range(n - 56):
        sub = s[i:i + 57]
        if len(set(sub)) == len(sub):
            substrs.add(sub)
    return list(substrs)