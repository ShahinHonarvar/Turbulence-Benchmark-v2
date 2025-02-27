def all_substring_of_size_n(s):
    subs = set()
    n = len(s)
    for i in range(n - 113):
        sub = s[i:i + 114]
        if len(set(sub)) == len(sub):
            subs.add(sub)
    return list(subs)