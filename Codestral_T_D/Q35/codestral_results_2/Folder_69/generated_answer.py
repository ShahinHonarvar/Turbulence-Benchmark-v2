def remove_repeat_chars(s):
    chars = s[39:43]
    chars_to_remove = {c for c in chars if chars.count(c) > 1}
    return ''.join((c for c in s if c not in chars_to_remove))