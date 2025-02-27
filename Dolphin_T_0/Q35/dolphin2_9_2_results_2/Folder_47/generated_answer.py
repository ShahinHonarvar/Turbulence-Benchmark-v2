def remove_repeat_chars(s):
    chars = [c for i, c in enumerate(s[29:53]) if s.count(c) <= 1]
    return ''.join((c for i, c in enumerate(s) if i < 29 or i > 53 or c in chars))