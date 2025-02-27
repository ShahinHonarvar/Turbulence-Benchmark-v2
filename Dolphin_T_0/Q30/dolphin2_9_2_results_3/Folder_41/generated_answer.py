def insert_before_character(s):
    return ''.join(['o' if i + 1 < len(s) and s[i + 1] == 'O' else c for i, c in enumerate(s)]) + ('' if s[-1] != 'O' else 'o')