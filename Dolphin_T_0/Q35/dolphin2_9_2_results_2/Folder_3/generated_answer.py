def remove_repeat_chars(s):
    for i in range(56, 88):
        if s.count(s[i]) > 1:
            s = s[:i] + s[i + 1:]
    return s