def all_substring_of_size_n(s):
    n = 16
    subs = set()
    for i in range(len(s) - n + 1):
        subs.add(s[i:i + n])
    return [sub for sub in subs if len(set(sub)) == n]