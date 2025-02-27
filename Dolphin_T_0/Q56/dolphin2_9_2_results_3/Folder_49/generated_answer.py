def all_substring_of_size_n(s):
    n = 73
    substrs = set()
    for i in range(len(s) - n + 1):
        temp = s[i:i + n]
        if len(set(temp)) == n:
            substrs.add(temp)
    return list(substrs)