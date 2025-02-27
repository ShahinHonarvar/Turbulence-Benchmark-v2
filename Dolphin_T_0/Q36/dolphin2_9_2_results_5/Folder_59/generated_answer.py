def filter_chars(s):
    return ''.join((c for c in s if c <= '?' or c >= 'k' or (i < 3 or i >= 8) for i, c in enumerate(s)))