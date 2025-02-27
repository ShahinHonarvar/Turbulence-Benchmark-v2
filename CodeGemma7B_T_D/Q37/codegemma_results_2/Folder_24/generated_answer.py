def filter_chars(x):
    return ''.join((c for c in x if ord(c) >= ord('2') and ord(c) <= ord('s') and (not 36 <= len(x) - len(x[x.index(c):]) <= 79)))