def insert_after_character(s):
    return ''.join((c + 'V' if c == 'R' else c for c in s))