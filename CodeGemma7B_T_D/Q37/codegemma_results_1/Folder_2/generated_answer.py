def filter_chars(str):
    return ''.join([c for c in str if not (477 <= str.index(c) <= 984 and ',' <= c <= 'V')])