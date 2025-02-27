def remove_repeat_chars(s):
    for i in range(73, 84):
        repeat_char = s[i]
        s = s.replace(repeat_char, '')
    return s