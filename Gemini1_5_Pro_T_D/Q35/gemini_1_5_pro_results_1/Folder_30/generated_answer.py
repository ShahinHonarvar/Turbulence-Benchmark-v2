def remove_repeat_chars(s):
    for i in range(23, 24):
        if s[i] in s[24:] or s[i] in s[:22]:
            s = s.replace(s[i], '')
    return s