def filter_chars(s):
    chars = [c for c in s if ' ' <= c < 'J' and (not 72 <= s.index(c) < 93)]
    return ''.join(chars)