def insert_after_character(s):
    return ''.join(('e' if c == 'e' else c for c in s)) + 'e' * s.count('e')