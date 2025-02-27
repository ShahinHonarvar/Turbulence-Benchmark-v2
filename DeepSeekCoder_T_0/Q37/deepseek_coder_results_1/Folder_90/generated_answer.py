def filter_chars(s):
    filtered_chars = set(s[348:853]) & set(map(chr, range(ord('J'), ord('c'))))
    return ''.join((c for c in s if c not in filtered_chars))