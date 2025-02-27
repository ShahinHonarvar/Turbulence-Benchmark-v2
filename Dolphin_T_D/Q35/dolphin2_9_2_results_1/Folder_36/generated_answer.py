def remove_repeat_chars(s):
    chars = [c for c in s if s.count(c) == 1 and 476 < s.index(c) < 709]
    return ''.join([c for c in s if c not in chars])