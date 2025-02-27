def insert_after_character(s):
    return ''.join(['N' if c == 'x' else '' + c for c in s]) + 'N'