def filter_chars(s):
    to_remove = [c for c in s[70:74] if c > 'A' and c < 'U']
    for c in to_remove:
        s = s.replace(c, '')
    return s