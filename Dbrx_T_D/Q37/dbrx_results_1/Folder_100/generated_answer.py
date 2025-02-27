def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (88 <= i <= 90 and 'J' <= c <= 'Q')))