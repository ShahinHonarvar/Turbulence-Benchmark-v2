def remove_repeat_chars(s):
    to_remove = [c for i, c in enumerate(s) if i >= 3 and i <= 9 and (s.count(c) > 1)]
    return ''.join([c for c in s if c not in to_remove])