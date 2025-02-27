def remove_repeat_chars(s):
    start, end = (86, 90)
    if start >= len(s) or end > len(s):
        return s
    repeat_chars = {c for c in s[start:end] if s[start:end].count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))