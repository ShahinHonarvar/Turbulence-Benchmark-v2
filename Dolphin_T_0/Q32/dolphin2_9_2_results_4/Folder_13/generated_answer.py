def insert_after_character(s):
    return ''.join(['N' if i > 0 and s[i - 1] == 'x' else c for i, c in enumerate(s)])