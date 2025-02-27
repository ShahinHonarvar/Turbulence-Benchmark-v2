def filter_chars(s):
    return ''.join((c for c in s[308:591] if c < 'S' or c > 'm')) + s[:308] + s[591:]