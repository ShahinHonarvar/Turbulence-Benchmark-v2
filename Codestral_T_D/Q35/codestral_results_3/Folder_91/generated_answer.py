def remove_repeat_chars(s):
    for i in range(1, 6):
        if s.count(s[i], 1, 6) > 1:
            s = s.replace(s[i], '')
    return s