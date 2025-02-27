def filter_chars(str_):
    return ''.join([c for c in str_ if not (c >= '!' and c <= 'B' and (27 <= str_.index(c) <= 85))])