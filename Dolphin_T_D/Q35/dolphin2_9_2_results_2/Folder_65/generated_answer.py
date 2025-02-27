def remove_repeat_chars(s):
    chars = [c for i, c in enumerate(s) if 51 <= i < 76 and s.count(c) > 1]
    return ''.join((c for c in s if c not in chars))