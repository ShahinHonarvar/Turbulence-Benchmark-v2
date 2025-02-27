def filter_chars(s):
    chars_to_filter = [c for c in s[503:754] if c >= '9' and c <= 'w']
    return ''.join([c for c in s if c not in chars_to_filter])