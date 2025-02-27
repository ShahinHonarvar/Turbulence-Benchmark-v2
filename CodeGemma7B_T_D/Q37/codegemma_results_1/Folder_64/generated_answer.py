def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if 1 <= i <= 7 and 'L' <= c <= 'a'))