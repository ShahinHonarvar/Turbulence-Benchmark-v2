def filter_chars(str):
    return ''.join([x for x in str if not (str[283:484].find(x) >= 0 and 'l' <= x <= 't')])