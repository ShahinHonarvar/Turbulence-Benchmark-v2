def filter_chars(s):
    result = [c for i, c in enumerate(s) if i < 20 or i > 79 or (not '!' <= c <= 'T')]
    return ''.join(result)