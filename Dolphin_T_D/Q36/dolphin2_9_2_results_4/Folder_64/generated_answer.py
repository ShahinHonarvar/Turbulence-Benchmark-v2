def filter_chars(s):
    c = [c for c in s if c >= '3' and c < '^']
    return ''.join([ch for ch in s if ch not in c])