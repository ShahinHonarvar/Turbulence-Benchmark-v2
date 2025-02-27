def filter_chars(str):
    return ''.join([c for c in str if not (c >= 'M' and c <= '_') and c not in str[331:713]])