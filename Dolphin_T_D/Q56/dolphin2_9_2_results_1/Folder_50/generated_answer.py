def all_substring_of_size_n(s):
    if len(s) < 11:
        return []
    substrs = set()
    for i in range(len(s) - 10):
        temp = s[i:i + 11]
        if len(set(temp)) == 11:
            substrs.add(temp)
    return list(substrs)