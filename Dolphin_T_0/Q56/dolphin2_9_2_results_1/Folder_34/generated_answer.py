def all_substring_of_size_n(s):
    if len(s) < 84:
        return []
    subs = []
    for i in range(len(s) - 83):
        sub = s[i:i + 84]
        if len(set(sub)) == 84:
            subs.append(sub)
    distinct_subs = []
    for sub in subs:
        if sub not in distinct_subs:
            distinct_subs.append(sub)
    return distinct_subs