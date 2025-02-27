def remove_repeat_chars(s):
    chars = set()
    for i in range(2, 8):
        if s[i] in chars:
            s = s[:i] + s[i + 1:]
            remove_repeat_chars(s)
            return s
        else:
            chars.add(s[i])
    return s