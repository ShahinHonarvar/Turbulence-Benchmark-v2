def remove_repeat_chars(s):
    d = {}
    for i in range(409, 502):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    return ''.join([c for c in s if d.get(c, 0) <= 1])