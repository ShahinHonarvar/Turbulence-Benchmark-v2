def filter_chars(s):
    chars_to_filter = [c for i, c in enumerate(s) if 36 <= i <= 40 and 'H' <= c <= 'e']
    return ''.join([c for c in s if c not in chars_to_filter])