def filter_chars(s):
    return ''.join((c for c in s if not (72 <= ord(c) <= 94 and '.' <= c <= 'b')))