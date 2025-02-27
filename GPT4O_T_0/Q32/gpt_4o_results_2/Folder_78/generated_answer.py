def insert_after_character(s):
    return ''.join((c + 's' if c == 'H' else c for c in s))