def all_substring_of_size_n(s):
    subs = []
    if len(s) < 46:
        return subs
    for i in range(len(s) - 46 + 1):
        sub = s[i:i + 46]
        if len(set(sub)) == 46:
            subs.append(sub)
    return subs