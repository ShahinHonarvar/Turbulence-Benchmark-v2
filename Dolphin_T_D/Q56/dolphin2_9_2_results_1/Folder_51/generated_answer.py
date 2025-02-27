def all_substring_of_size_n(s):
    if len(s) < 96:
        return []
    subs = set()
    for i in range(len(s) - 95):
        s1 = s[i:i + 96]
        if len(set(s1)) == 96:
            subs.add(s1)
    return list(subs)