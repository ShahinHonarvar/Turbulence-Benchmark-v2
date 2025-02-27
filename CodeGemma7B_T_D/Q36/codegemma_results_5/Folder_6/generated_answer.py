def filter_chars(string):
    return ''.join((c for c in string if not (c > 'B' and c < 'v' and (31 <= ord(c) <= 70))))