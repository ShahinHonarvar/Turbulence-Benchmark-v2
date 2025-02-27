def insert_after_character(s):
    return ''.join((c + 'n' if c == 'w' else c for c in s))