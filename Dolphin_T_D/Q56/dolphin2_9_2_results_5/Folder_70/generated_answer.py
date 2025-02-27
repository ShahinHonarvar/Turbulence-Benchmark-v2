def all_substring_of_size_n(s):
    n = 12
    subs = []
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if len(set(sub)) == n:
            subs.append(sub)
    return subs