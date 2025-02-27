def filter_chars(s):
    chars_to_filter = [c for c in s[29:33] if '%' < c < 'a']
    return ''.join((c for c in s if c not in chars_to_filter))