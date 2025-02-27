def remove_repeat_chars(s):
    to_remove = {c for c in s[44:91] if s.count(c) > 1}
    return ''.join((c for c in s if c not in to_remove))