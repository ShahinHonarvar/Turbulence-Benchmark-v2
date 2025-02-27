def all_substring_of_size_n(s):
    subs = set()
    for i in range(len(s) - 2):
        sub = s[i:i + 3]
        if len(set(sub)) == len(sub):
            subs.add(sub)
    return list(subs)