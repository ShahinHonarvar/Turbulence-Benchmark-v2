def all_substring_of_size_n(s):
    subs = set()
    for i in range(len(s) - 8):
        sub = s[i:i + 9]
        if len(set(sub)) == 9:
            subs.add(sub)
    return list(subs)