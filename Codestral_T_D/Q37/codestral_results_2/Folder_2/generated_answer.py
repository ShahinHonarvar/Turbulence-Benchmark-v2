def filter_chars(s):
    return ''.join((char for i, char in enumerate(s) if not (477 <= i <= 984 and ',' <= char <= 'V')))