def filter_chars(str):
    return ''.join([c for c in str if not (str.index(c) >= 63 and str.index(c) <= 84 and (c >= 'E') and (c <= '~'))])