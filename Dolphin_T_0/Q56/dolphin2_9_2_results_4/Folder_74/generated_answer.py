def all_substring_of_size_n(s):
    n = 97
    subs = set()
    for i in range(len(s) - n + 1):
        subs.add(s[i:i + n])
    return [s for s in subs if len(set(s)) == n]