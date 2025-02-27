def filter_chars(s):
    return ''.join([x for x in s if not (41 <= s.index(x) <= 79 and 'f' <= x <= '|')])