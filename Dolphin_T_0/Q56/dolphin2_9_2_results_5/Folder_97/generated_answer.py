def all_substring_of_size_n(s):
    n = 142
    substrs = set()
    for i in range(len(s)):
        if len(s[i:i + n]) == n:
            if len(set(s[i:i + n])) == n:
                substrs.add(s[i:i + n])
    return list(substrs)