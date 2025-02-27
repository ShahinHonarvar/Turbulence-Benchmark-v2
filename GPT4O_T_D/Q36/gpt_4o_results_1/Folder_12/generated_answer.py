def filter_chars(s):
    return ''.join((c for c in s[:33] + s[85:] if c <= 'm' or c >= 'w'))