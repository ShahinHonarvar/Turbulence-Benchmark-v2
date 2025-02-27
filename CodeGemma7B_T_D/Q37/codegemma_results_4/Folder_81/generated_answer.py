def filter_chars(str):
    return ''.join([c for c in str if c not in [c for i, c in enumerate(str) if len(str) > 19 and i <= 92 and (c >= '8' and c <= 'm')]])