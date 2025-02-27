def insert_after_character(s):
    return ''.join(('P' if i > 0 and s[i - 1] == 'C' else c for i, c in enumerate(s))) + ('' if s[-1] != 'C' else 'P')