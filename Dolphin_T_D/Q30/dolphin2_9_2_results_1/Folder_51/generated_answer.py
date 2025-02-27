def insert_before_character(s):
    return ''.join(['O' if c == 'o' and i > 0 and (s[i - 1] != 'O') else c for i, c in enumerate(s)]) + ('O' if s[-1] == 'o' else '')