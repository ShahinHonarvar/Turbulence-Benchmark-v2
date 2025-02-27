def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (41 <= i <= 79 and 'f' <= c <= '|') or not 41 <= i <= 79))