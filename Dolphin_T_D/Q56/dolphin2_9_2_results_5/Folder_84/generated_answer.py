def all_substring_of_size_n(s):
    n = 114
    subs = set()
    for i in range(len(s)):
        if len(s[i:i + n]) == n:
            subs.add(s[i:i + n])
    return list(subs)