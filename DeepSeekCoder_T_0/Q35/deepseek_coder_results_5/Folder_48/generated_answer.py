def remove_repeat_chars(s):
    start, end = (409, 502)
    repeat_chars = {c for i, c in enumerate(s) if start < i < end and s.count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))