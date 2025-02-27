def insert_after_character(s):
    return ''.join((c + 'w' if c == 's' else c for c in s))