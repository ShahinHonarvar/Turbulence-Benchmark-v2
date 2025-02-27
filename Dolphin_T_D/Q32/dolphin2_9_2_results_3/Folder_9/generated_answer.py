def insert_after_character(s):
    return ''.join(['E' if i > 0 and s[i - 1] == 'e' else c for i, c in enumerate(s)])