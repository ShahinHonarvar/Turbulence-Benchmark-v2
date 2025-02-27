def filter_chars(s):
    result = [c for i, c in enumerate(s) if i < 19 or i > 90 or c < 'F' or (c > 'h')]
    return ''.join(result)