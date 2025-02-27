def all_substring_of_size_n(s):
    substrs = []
    for i in range(len(s) - 59):
        sub = s[i:i + 60]
        if len(set(sub)) == 60:
            substrs.append(sub)
    return substrs