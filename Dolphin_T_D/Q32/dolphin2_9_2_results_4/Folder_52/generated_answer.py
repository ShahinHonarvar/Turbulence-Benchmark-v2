def insert_after_character(s):
    return ''.join(('T' if c == 'T' else '' if c == 'V' else c for c in s)) + 'V'