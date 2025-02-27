def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 348 or i > 852 or (c < 'J' or c > 'b')))