def filter_chars(str):
    new_str = [c for c in str if c > '/' and c < '6']
    return ''.join(new_str)