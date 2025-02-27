def remove_repeat_chars(s):
    to_remove = {c for i, c in enumerate(s[57:84], start=57) if s.count(c) > 1 and 57 <= i < 84}
    return ''.join((c for c in s if c not in to_remove))