def insert_after_character(s):
    return ''.join(('O' if c == 'O' and s[i + 1] != 'O' else c + 'O' if c == 'O' else c for i, c in enumerate(s)))