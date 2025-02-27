def filter_chars(s):
    if len(s) < 41:
        return s
    start, end = (41, min(64, len(s) - 1))
    chars_to_remove = {c for c in s[start:end + 1] if 'K' <= c <= ']'}
    return ''.join((c for c in s if c not in chars_to_remove))