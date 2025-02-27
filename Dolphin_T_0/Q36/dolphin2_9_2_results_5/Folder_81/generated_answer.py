def filter_chars(s):
    return ''.join((c for c in s if c < '5' or c > 'f' or (c >= '6' and c <= 'f')))