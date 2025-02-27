def all_substring_of_size_n(s):
    n = 130
    subs = set()
    for i in range(len(s) - n + 1):
        sub_s = s[i:i + n]
        if len(set(sub_s)) == n:
            subs.add(sub_s)
    return list(subs)