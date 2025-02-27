def insert_after_character(s):
    return ''.join((c + 'f' if c == 'E' else c for c in s))