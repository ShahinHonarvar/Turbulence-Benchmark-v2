def filter_chars(s):
    chars_to_remove = [c for c in s[348:852] if c >= 'J' and c <= 'b']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s