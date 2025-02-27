def remove_repeat_chars(s):
    chars = {}
    for i in range(32, 44):
        for c in s:
            if i == ord(c):
                if c not in chars:
                    chars[c] = 1
                else:
                    chars[c] += 1
    for c in chars:
        if chars[c] > 1:
            s = s.replace(c, '')
    return s