def all_substring_of_size_n(s):
    n = 18
    substrs = []
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            if len(set(s[i:j])) == n:
                substrs.append(s[i:j])
    return substrs