def all_substring_of_size_n(s):
    n = 37
    subs = []
    for i in range(len(s) - n + 1):
        subs_set = s[i:i + n]
        if len(set(subs_set)) == n:
            subs.append(subs_set)
    return list(set(subs))