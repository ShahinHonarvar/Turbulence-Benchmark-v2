def filter_chars(string):
    return ''.join([c for c in string if not (55 < ord(c) < 80 and 'S' <= c <= 's')])