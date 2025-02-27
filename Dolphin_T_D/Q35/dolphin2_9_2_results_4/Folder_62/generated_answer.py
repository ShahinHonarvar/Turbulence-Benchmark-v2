def remove_repeat_chars(s):
    chars = {}
    for c in s[50:92]:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    for c in list(chars):
        if chars[c] > 1:
            s = s.replace(c, '')
    return s