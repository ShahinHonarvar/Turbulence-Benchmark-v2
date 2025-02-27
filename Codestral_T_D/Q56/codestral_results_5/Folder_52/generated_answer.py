def all_substring_of_size_n(s):
    n = 15
    substrs = []
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substr = s[i:j]
            if len(substr) == len(set(substr)):
                substrs.append(substr)
    return list(set(substrs))