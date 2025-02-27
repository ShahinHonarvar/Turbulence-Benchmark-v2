def insert_before_character(s):
    return ''.join(('N' if c == 'x' else c for c in s)) + 'N' if s[-1] != 'x' else ''