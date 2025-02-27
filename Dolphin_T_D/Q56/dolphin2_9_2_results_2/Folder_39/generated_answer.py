def all_substring_of_size_n(s):
    subs = []
    n = len(s)
    for i in range(n - 93):
        sub = s[i:i + 94]
        if len(set(sub)) == len(sub):
            subs.append(sub)
    return subs