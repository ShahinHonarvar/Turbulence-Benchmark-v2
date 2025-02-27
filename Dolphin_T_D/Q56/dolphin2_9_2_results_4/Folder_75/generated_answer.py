def all_substring_of_size_n(s):
    subs = set()
    n = 16
    for i in range(len(s)):
        if len(s[i:i + n]) == n:
            subs.add(s[i:i + n])
    subs = [x for x in subs if len(set(x)) == n]
    return list(subs)