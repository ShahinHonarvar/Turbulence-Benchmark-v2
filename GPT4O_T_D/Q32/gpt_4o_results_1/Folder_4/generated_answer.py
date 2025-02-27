def insert_after_character(s):
    return ''.join((c + ('6' if c == 'a' else '') for c in s))