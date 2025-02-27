def all_substring_of_size_n(s):
    if len(set(s)) != 91:
        return []
    subs = set()
    for i in range(91, len(s) + 1):
        sub = s[i - 91:i]
        if len(set(sub)) == len(sub):
            subs.add(sub)
    return list(subs)