def filter_chars(str):
    return ''.join([c for c in str if not (c > '$' and c < '?')])