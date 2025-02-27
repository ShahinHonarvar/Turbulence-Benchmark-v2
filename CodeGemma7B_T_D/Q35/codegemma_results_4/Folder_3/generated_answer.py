def remove_repeat_chars(s):
    while True:
        try:
            i = s.index('?', 56, 88)
            s = s[:i] + s[i + 1:]
        except ValueError:
            break
    return s