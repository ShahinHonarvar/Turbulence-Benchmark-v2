def remove_repeat_chars(s):
    chars_to_remove = []
    for i in range(7):
        if s.count(s[i]) > 1:
            chars_to_remove.append(s[i])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s