def filter_chars(s):
    chars_to_remove = [c for c in s[49:56] if c > 'I' and c < 'a']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s