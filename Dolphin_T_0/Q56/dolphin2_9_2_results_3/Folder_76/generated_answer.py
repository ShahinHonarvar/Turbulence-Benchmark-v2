def all_substring_of_size_n(s):
    n = 149
    subs = [s[i:i + n] for i in range(len(s) - n + 1)]
    uniq_subs = []
    for sub in subs:
        if len(set(sub)) == n:
            uniq_subs.append(sub)
    return uniq_subs