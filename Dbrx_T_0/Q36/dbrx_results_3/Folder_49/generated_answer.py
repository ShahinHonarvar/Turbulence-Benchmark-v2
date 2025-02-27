def filter_chars(s):
    return ''.join((c for c in s if 46 < s.index(c) < 91 and (not 'D' < c < 'H')))