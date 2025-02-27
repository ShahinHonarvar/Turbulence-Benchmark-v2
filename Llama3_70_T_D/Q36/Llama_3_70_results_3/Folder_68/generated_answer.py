def filter_chars(s):
    chars_to_filter = set(s[1:9])
    chars_to_filter = {c for c in chars_to_filter if '8' < c < 'm'}
    return ''.join((c for c in s if c not in chars_to_filter))