def filter_chars(string):
    return ''.join([c for c in string if (c < 'D' or c > 'H') or c < 46 or c >= 91])