def remove_repeat_chars(s):
    for c in set(s[27:96]):
        if s[27:96].count(c) > 1:
            s = s.replace(c, '')
    return s