def remove_repeat_chars(s):
    to_remove = [c for c in s[45:49] if s[45:49].count(c) > 1]
    for c in to_remove:
        s = s.replace(c, '')
    return s