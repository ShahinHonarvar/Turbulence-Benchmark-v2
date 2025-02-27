def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(43, 70):
        if s[i] in s[i + 1:]:
            repeat_chars.add(s[i])
    for c in repeat_chars:
        s = s.replace(c, '')
    return s