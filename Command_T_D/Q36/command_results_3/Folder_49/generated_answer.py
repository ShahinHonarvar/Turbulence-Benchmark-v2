def filter_chars(s):
    return s.translate(str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDEFGHIJ'))