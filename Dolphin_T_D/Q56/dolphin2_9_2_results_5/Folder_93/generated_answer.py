def all_substring_of_size_n(s):
    if len(s) < 54:
        return []
    substrs = set()
    for i in range(len(s) - 53):
        if len(set(s[i:i + 54])) == 54:
            substrs.add(s[i:i + 54])
    return list(substrs)