def filter_chars(str):
    return ''.join([c for c in str if not (82 < ord(c) < 89 and '*' < c < '[')])