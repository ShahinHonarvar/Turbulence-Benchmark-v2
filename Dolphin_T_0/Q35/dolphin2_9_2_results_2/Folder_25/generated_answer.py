def remove_repeat_chars(s):
    chars = [c for c in s[37:43]]
    for c in chars:
        if chars.count(c) > 1:
            s = ''.join([char for char in s if char != c])
    return s