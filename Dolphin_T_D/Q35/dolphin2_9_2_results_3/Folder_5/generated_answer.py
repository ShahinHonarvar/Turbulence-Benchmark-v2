def remove_repeat_chars(s):
    to_remove = [c for i, c in enumerate(s) if i < 2 or i > 8 or s.count(c) == 1]
    return ''.join([c for c in s if c not in to_remove])