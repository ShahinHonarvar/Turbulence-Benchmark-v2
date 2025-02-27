def remove_repeat_chars(s):
    for c in s[13:91]:
        if s[13:91].count(c) > 1:
            s = s.replace(c, '')
    return s