def insert_after_character(s):
    return ''.join(('e' if i > 0 and s[i - 1] == 'E' else c for i, c in enumerate(s)))