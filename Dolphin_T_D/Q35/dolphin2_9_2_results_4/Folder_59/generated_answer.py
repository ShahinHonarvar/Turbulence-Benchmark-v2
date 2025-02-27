def remove_repeat_chars(s):
    s = list(s)
    repeat_chars = [c for c in s[0:10] if s.count(c) > 1]
    s = [c for c in s if c not in repeat_chars]
    return ''.join(s)