def insert_after_character(s):
    return ''.join(['t' if i > 0 and s[i - 1] == 'a' else c for i, c in enumerate(s)])