def remove_repeat_chars(s):
    chars = [s[i] for i in range(3, 8)]
    for char in chars:
        if chars.count(char) > 1:
            s = s.replace(char, '')
    return s