def all_substring_of_size_n(s):
    if len(s) < 94:
        return []
    subs = set()
    for i in range(len(s) - 93):
        sub = s[i:i + 94]
        if len(set(sub)) == len(sub):
            subs.add(sub)
    return list(subs)