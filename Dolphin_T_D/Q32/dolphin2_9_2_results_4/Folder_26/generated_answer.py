def insert_after_character(s):
    return ''.join(('w' if i > 0 and s[i - 1] == 'r' else c for i, c in enumerate(s)))