def remove_repeat_chars(s):
    d = dict.fromkeys(s, 0)
    for i in range(len(s)):
        if i >= 0 and i <= 10:
            d[s[i]] += 1
    for k, v in d.items():
        for _ in range(v - 1):
            s = s.replace(k, '', 1)
    return s