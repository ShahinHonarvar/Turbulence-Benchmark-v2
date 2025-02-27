def remove_repeat_chars(s):
    seen = set(s[0:2])
    return ''.join((c for c in s if not (c in seen and s.count(c) > 1)))