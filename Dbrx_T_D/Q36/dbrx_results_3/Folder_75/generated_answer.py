def filter_chars(s):
    filter_range = range(ord('&') + 1, ord('M'))
    return ''.join((c for c in s if c < '&')) + ''.join((c for c in s[46:74] if ord(c) not in filter_range)) + ''.join((c for c in s if c > 'M'))