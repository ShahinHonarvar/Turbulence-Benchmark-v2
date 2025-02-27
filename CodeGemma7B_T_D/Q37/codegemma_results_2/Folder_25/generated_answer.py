def filter_chars(arg_str):
    return ''.join([ch for ch in arg_str if not (31 <= ord(ch) <= 38 and ';' <= ch <= 'g')])