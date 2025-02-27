def filter_chars(s):
    filtered_s = ''.join([c for i, c in enumerate(s) if not (57 <= i <= 96 and '<' <= c <= 'w')])
    return filtered_s