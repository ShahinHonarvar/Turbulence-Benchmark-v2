def filter_chars(s):
    chars_to_filter = [c for i, c in enumerate(s) if 503 <= i <= 753 and '9' <= c <= 'w']
    return ''.join((c for c in s if c not in chars_to_filter))