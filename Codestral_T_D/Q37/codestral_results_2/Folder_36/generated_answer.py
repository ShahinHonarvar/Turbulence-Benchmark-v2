def filter_chars(s):
    filtered_chars = [c for c in set(s[259:503]) if ',' <= c <= '3']
    return ''.join((c for c in s if c not in filtered_chars))