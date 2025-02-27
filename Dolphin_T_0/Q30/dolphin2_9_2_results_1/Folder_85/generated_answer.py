def insert_before_character(s):
    return ''.join(['a' if i + 1 == s.index('o') else c for i, c in enumerate(s)])