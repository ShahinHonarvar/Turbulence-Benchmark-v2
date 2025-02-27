def all_substring_of_size_n(s):
    n = len(s)
    subs = []
    for i in range(n):
        for j in range(i + 75, n):
            sub = s[i:j]
            if len(set(sub)) == len(sub):
                subs.append(sub)
    return subs