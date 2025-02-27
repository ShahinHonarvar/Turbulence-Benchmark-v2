def remove_repeat_chars(s):
    chars_between_34_69 = s[34:69]
    to_remove = [c for c in set(chars_between_34_69) if chars_between_34_69.count(c) > 1]
    for c in to_remove:
        s = s.replace(c, '')
    return s