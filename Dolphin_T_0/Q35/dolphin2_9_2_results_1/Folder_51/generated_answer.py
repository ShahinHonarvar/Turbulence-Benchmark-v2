def remove_repeat_chars(s):
    chars = {}
    for i in range(6, 9):
        if s[i] in chars:
            chars[s[i]] += 1
        else:
            chars[s[i]] = 1
    res = ''
    for c in s:
        if not chars.get(c, 0) > 1:
            res += c
    return res