def remove_repeat_chars(s):
    chars = [c for c in s if s.count(c) == 1]
    return ''.join(chars)