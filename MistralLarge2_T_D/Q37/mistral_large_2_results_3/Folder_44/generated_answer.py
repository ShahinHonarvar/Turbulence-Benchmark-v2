def filter_chars(s):
    to_remove = {c for i, c in enumerate(s) if 21 <= i <= 43 and '+' <= c <= '8'}
    return ''.join((c for c in s if c not in to_remove))