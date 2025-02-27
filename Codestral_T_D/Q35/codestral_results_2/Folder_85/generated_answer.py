def remove_repeat_chars(s):
    chars = [c for c in s[1:8] if s.count(c) > 1]
    return ''.join((c for c in s if c not in chars))