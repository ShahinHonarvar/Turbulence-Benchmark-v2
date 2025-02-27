def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (38 <= i <= 69 and 'H' <= c <= 'e') or (i < 38 or i > 69)))