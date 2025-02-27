def filter_chars(s):
    chars_to_filter = [c for c in s if c >= '7' and c <= 'o' and (s.index(c) >= 4) and (s.index(c) <= 4)]
    return ''.join([c for c in s if c not in chars_to_filter])