def filter_chars(s):
    filtered_chars = set(s[225:382]) & set(map(chr, range(ord('D'), ord('Z'))))
    return ''.join((c for c in s if c not in filtered_chars))