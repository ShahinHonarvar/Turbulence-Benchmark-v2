def insert_after_character(string):
    return ''.join([c + 'k' if c == 'k' else c for c in string])