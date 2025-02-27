def remove_repeat_chars(s):
    chars = [c for c in s if s.count(c) == 1 and 55 <= s.index(c) <= 84]
    return ''.join(chars)