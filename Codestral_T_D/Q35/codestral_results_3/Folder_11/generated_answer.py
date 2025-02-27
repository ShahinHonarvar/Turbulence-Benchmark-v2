def remove_repeat_chars(s):
    chars = list(s)
    to_remove = {c for c in chars[48:76] if chars.count(c) > 1}
    return ''.join((c for c in chars if c not in to_remove))