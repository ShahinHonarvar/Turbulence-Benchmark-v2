def filter_chars(s):
    excluded_chars = {s[i] for i in range(41, 65) if 'K' <= s[i] <= ']'}
    return ''.join((c for c in s if c not in excluded_chars))