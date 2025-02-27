def remove_repeat_chars(s):
    d = {}
    for i in range(43, 70):
        if s[i] in d:
            while s[i] in s:
                s = s[:i] + s[i + 1:]
        else:
            d[s[i]] = i
    return s