def filter_chars(s):
    chars_to_filter = [c for i, c in enumerate(s) if 42 < i < 67 and '6' < c < 'g']
    return ''.join([c for c in s if c not in chars_to_filter])