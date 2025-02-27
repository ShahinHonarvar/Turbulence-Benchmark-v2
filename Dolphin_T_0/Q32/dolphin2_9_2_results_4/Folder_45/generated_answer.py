def insert_after_character(s):
    return ''.join(('O' if c == 'O' and i != len(s) - 1 else c for i, c in enumerate(s))) + 'O' if s[-1] == 'O' else s