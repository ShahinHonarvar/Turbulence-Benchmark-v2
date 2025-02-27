def all_substring_of_size_n(s):
    subs = set()
    for i in range(len(s) - 148):
        sub = s[i:i + 149]
        if len(sub) == len(set(sub)):
            subs.add(sub)
    return list(subs)