def filter_chars(s):
    to_remove = [c for c in s[11:73] if c >= 'i' and c <= 'v']
    for c in to_remove:
        s = s.replace(c, '')
    return s