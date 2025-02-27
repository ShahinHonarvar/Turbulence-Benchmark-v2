def insert_after_character(s):
    return ''.join(('w' if i == s.index('s', i) else c for i, c in enumerate(s)))