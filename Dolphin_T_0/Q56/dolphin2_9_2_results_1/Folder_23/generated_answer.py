def all_substring_of_size_n(s):
    n = 42
    substrs = set()
    for i in range(len(s) - n + 1):
        if len(set(s[i:i + n])) != n:
            continue
        substrs.add(s[i:i + n])
    return list(substrs)