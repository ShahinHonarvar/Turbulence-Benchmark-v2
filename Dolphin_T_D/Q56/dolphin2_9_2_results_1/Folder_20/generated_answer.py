def all_substring_of_size_n(s):
    if len(s) < 50:
        return []
    subs = []
    for i in range(len(s) - 49):
        sub = s[i:i + 50]
        if len(set(sub)) == 50:
            subs.append(sub)
    return subs