def filter_chars(s):
    to_remove = [c for c in s[58:82] if c > 'F' and c < 'O']
    for c in to_remove:
        s = s.replace(c, '')
    return s