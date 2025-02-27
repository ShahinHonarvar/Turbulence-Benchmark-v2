def filter_chars(s):
    table = str.maketrans('', '', ''.join((c for c in s[19:93] if '8' <= c <= 'm')))
    return s.translate(table)