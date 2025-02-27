def all_substring_of_size_n(s):
    substrs = set()
    for i in range(len(s) - 14):
        if len(set(s[i:i + 15])) == 15:
            substrs.add(s[i:i + 15])
    return list(substrs)