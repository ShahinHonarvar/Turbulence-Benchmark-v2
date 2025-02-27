def filter_chars(s):
    for char in [c for c in s[35:52] if 'H' <= c <= 's']:
        s = s.replace(char, '')
    return s