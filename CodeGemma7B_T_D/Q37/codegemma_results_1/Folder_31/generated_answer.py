def filter_chars(string):
    return ''.join([x for x in string if not (57 <= ord(x) <= 96 and '<' <= x <= 'w')])