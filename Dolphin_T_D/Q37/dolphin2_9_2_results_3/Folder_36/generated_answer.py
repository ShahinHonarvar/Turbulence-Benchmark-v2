def filter_chars(s):
    return ''.join([c for c in s if c not in s[259:502] and ',' <= c <= '3'])