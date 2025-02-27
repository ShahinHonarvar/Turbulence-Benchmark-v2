def remove_repeat_chars(s):
    chars = [c for i, c in enumerate(s) if 25 < i < 80 and s.count(c) > 1]
    return ''.join([c for c in s if c not in chars])