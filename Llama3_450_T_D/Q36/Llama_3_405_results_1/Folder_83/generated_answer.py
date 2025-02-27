def filter_chars(s):
    chars_to_filter = set(s[72:93])
    chars_to_filter = {c for c in chars_to_filter if '<' < c < 'J'}
    return ''.join([c for c in s if c not in chars_to_filter])