def filter_chars(s):
    for char in s[38:100]:
        if 'A' <= char <= 'Q':
            s = ''.join((c for c in s if c != char))
    return s