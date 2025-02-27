def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if 20 <= i <= 62 and 'i' <= c <= 'k' or i < 20 or i > 62))