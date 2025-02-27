def filter_chars(s):
    chars_to_filter = [c for c in s[22:86] if '7' <= c <= 'e']
    return ''.join(filter(lambda c: c not in chars_to_filter, s))