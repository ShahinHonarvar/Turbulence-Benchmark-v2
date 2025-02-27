def insert_before_character(v):
    ch = 'O'
    return ''.join((c + (ch if c == ch else '') for c in v))