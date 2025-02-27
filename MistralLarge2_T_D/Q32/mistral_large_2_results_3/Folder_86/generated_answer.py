def insert_after_character(s):
    return ''.join((c + ('Q' if c == 'O' else '') for c in s))