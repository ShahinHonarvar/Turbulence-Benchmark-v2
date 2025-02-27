def insert_after_character(s):
    return ''.join((c + ('V' if c == 'T' else '') for c in s))