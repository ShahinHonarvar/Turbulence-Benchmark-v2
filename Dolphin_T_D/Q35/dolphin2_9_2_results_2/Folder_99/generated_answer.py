def remove_repeat_chars(s):
    chars_to_remove = []
    for c in s[450:905]:
        if s.count(c) > 1:
            chars_to_remove.append(c)
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s