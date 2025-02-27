def insert_after_character(s):
    return ''.join(['R' + 'V' if c == 'R' else c for c in s])