def filter_chars(s):
    chars_to_filter = [c for c in s[19:93] if c >= '8' and c <= 'm']
    return ''.join([c for c in s if c not in chars_to_filter])