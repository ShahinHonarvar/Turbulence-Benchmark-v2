def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 603 or i > 759 or (not 'Q' <= c <= 'h')))