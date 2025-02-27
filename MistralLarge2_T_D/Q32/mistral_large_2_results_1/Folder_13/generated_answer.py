def insert_after_character(s):
    return ''.join((c + ('N' if c == 'x' else '') for c in s))