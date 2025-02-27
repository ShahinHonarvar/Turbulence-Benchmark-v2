def insert_after_character(s):
    return ''.join((c + ('4' if c == 'Y' else '') for c in s))