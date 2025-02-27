def filter_chars(s):
    chars_to_remove = [c for c in s[36:80] if c >= '2' and c <= 's']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s