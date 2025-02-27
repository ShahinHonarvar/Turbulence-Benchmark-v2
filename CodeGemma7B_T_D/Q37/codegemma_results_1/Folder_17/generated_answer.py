def filter_chars(s):
    return ''.join([x for x in s if not (27 <= s.index(x) <= 29 and ';' <= x <= 'b')])