def all_substring_of_size_n(s):
    n = 48
    subs = []
    for i in range(len(s)):
        if i + n <= len(s):
            subs = subs + [s[i:i + n]]
    subs = list(filter(lambda sub: len(set(sub)) == len(sub), subs))
    subs = list(filter(lambda sub: sub not in subs[:subs.index(sub)], subs))
    return subs