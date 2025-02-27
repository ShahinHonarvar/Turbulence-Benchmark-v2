def insert_after_character(s):
    return ''.join([c + ('V' if c == 'P' else '') for c in s])