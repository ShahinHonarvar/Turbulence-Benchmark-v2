def all_substring_of_size_n(s):
    subs = set()
    for i in range(len(s) - 61):
        sub = s[i:i + 63]
        if len(set(sub)) == 63:
            subs.add(sub)
    return list(subs)