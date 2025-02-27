def insert_after_character(s):
    return ''.join(('K' if c == ' ' else c for c in s)) + 'K'