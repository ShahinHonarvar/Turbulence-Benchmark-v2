def all_substring_of_size_n(s):
    n = len(s)
    subs = set()
    for i in range(n - 11):
        sub = ''.join(sorted(s[i:i + 12]))
        if len(set(sub)) == len(sub):
            subs.add(sub)
    return list(subs)