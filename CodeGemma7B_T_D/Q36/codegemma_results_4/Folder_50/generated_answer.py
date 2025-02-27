def filter_chars(s):
    return ''.join(filter(lambda c: c not in range(62, 88) or (c > '%' and c < 'q'), s))