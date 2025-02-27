def all_substring_of_size_n(s):
    substrs = []
    for i in range(len(s) - 57):
        sub = s[i:i + 58]
        if len(set(sub)) == len(sub):
            substrs.append(sub)
    return list(set(substrs))