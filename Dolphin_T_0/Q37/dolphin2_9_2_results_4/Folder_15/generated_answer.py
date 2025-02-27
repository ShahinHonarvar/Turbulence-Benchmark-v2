def filter_chars(s):
    chars = [s[i] for i in range(2, 7) if s[i] >= '?' and s[i] <= 'f']
    return ''.join((c for c in s if c not in chars))