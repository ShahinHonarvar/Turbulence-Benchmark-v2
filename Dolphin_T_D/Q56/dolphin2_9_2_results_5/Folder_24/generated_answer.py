def all_substring_of_size_n(s):
    subs = set()
    n = 52
    for i in range(len(s) - n + 1):
        subs.add(s[i:i + n])
    subs = [x for x in subs if len(set(x)) == len(x)]
    return list(subs) if subs else []