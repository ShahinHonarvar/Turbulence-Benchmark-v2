def filter_chars(string):
    return ''.join([c for c in string if not (c in string[1:5 + 1] and (c >= '$' and c <= ';'))])