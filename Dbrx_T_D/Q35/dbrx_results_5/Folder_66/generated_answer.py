def remove_repeat_chars(s):
    chars_to_remove = {c for i, c in enumerate(s) if 10 < i < 76 and s.count(c, i) > 1}
    return ''.join((c for i, c in enumerate(s) if i < 10 or i >= 76 or c not in chars_to_remove))