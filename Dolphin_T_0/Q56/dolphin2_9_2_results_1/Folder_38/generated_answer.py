def all_substring_of_size_n(s):
    subs = set()
    for i in range(len(s) - 34):
        sub = s[i:i + 35]
        if len(set(sub)) == len(sub):
            subs.add(sub)
    return list(subs)