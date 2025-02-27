def remove_repeat_chars(s):
    to_remove = [c for c in set(s[:4]) if s.count(c) > 1]
    for c in to_remove:
        s = s.replace(c, '')
    return s