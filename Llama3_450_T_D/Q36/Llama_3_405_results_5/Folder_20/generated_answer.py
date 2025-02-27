def filter_chars(s):
    chars_to_filter = [c for i, c in enumerate(s) if 13 < i < 40 and ':' < c < 'C']
    return ''.join([c for c in s if c not in chars_to_filter])