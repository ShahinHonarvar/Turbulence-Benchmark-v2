def insert_after_character(s):
    return ''.join((c + ('m' if c == 'F' else '') for c in s))