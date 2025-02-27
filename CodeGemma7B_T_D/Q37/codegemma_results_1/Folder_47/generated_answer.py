def filter_chars(s):
    return ''.join([c for c in s if not (38 <= len(s) - 1 <= 54 and c >= ':' and (c <= 'r'))])