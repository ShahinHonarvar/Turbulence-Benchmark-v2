def remove_repeat_chars(s):
    return ''.join([c for i, c in enumerate(s) if i < 13 or i > 69 or s.index(c) == i])