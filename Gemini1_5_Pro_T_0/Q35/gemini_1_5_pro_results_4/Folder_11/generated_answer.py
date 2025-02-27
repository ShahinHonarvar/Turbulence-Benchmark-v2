def remove_repeat_chars(s):
    for i in range(48, 76):
        if s.count(s[i]) > 1:
            s = s.replace(s[i], '')
    return s