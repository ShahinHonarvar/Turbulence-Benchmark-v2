def insert_after_character(s):
    return ''.join((c + 'H' if c == 'C' else c for c in s))