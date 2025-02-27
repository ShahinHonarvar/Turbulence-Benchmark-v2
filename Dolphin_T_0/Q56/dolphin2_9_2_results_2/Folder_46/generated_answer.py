def all_substring_of_size_n(s):
    if len(set(s)) == 1:
        return []
    subs = []
    for i in range(len(s) - 86):
        sub = s[i:i + 87]
        if len(set(sub)) == len(sub):
            subs.append(sub)
    return subs