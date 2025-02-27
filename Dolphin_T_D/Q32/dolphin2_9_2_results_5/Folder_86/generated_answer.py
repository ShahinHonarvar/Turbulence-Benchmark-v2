def insert_after_character(s):
    return ''.join(('Q' if i > 0 and s[i - 1] == 'O' else c for i, c in enumerate(s)))