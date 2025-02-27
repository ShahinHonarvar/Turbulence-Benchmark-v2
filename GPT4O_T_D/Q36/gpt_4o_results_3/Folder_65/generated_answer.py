def filter_chars(s):
    if len(s) <= 58:
        return s
    start = max(59, 0)
    end = min(82, len(s) - 1)
    chars_to_remove = {c for c in s[start:end] if 'F' < c < 'O'}
    return ''.join((c for c in s if c not in chars_to_remove))