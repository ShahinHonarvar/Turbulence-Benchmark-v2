def filter_chars(s):
    chars_to_filter = [c for c in s[18:38] if ')' < c < 'P']
    return ''.join([c for c in s if c not in chars_to_filter])