def remove_repeat_chars(s):
    i = 3
    while i < 9:
        if s[i] in s[i + 1:9]:
            s = s.replace(s[i], '')
            i = 3
        else:
            i += 1
    return s