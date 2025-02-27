def all_substring_of_size_n(s):
    subs = set()
    for i in range(len(s) - 76):
        sub = s[i:i + 77]
        if len(set(sub)) == len(sub):
            subs.add(sub)
    return list(subs)