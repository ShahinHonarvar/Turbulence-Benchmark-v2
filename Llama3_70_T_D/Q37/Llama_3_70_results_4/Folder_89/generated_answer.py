def filter_chars(s):
    filtered = {}
    for i in range(11, 33):
        c = ord(s[i])
        if 33 <= c <= 64:
            filtered[chr(c)] = 1
    res = ''
    for c in s:
        if c not in filtered:
            res += c
    return res