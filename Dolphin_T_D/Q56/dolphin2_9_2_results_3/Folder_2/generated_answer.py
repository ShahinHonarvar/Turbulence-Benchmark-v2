def all_substring_of_size_n(s):
    subs = set()
    for i in range(len(s) - 55):
        sub = s[i:i + 56]
        if len(set(sub)) == 56:
            subs.add(sub)
    return list(subs)