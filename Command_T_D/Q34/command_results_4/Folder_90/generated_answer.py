def find_original_set(s):
    s.sort()
    res = s[0]
    for i in range(1, len(s)):
        res |= s[i]
    return res