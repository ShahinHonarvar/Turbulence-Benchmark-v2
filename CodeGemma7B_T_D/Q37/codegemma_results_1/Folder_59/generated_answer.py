def filter_chars(x):
    return ''.join([a for a in x[:4] + x[5:] if not (a >= '5' and a <= '_')]) + x[4:5] + ''.join([a for a in x[6:] if not (a >= '5' and a <= '_')])