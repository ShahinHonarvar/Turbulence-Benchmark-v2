def insert_after_character(s):
    return ''.join((c + 'y' if c == 'b' else c for c in s))