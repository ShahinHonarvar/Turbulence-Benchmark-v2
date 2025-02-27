def filter_chars(i):
    return ''.join([x for x in i if not ('!' < x < 's' and [i.index(x) for i, x in enumerate(i) if 81 <= i < 86])])