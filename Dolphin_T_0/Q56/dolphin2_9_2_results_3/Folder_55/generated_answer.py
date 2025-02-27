def all_substring_of_size_n(s):
    length = len(s)
    if length < 40:
        return []
    subs = []
    for i in range(0, length - 39):
        sub = s[i:i + 40]
        if len(set(sub)) == 40 and sub not in subs:
            subs.append(sub)
    if len(subs) == 0:
        return []
    return subs