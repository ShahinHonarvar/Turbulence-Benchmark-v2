def filter_chars(s):
    to_filter = [c for c in s if 348 <= s.index(c) <= 852 and 'J' <= c <= 'b']
    for c in to_filter:
        s = s.replace(c, '')
    return s