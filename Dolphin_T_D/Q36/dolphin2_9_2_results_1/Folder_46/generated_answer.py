def filter_chars(s):
    to_remove = [c for c in s[19:69] if c > '<' and c < 'C']
    for c in to_remove:
        s = s.replace(c, '')
    return s