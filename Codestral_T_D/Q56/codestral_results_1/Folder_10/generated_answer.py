def all_substring_of_size_n(s):
    n = 5
    subs = []
    for i in range(len(s)):
        if len(s[i:i + n]) == n and len(set(s[i:i + n])) == n:
            subs.append(s[i:i + n])
    return subs