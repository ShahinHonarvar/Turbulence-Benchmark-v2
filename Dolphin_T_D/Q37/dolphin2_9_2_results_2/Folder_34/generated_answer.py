def filter_chars(s):
    to_remove = [c for c in s if 54 <= s.index(c) <= 62 and ')' <= c <= '9']
    return ''.join([c for c in s if c not in to_remove])