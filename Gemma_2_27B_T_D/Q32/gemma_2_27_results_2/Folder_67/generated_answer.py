def insert_after_character(s):
    return ''.join([c + '1' if c == 'j' else c for c in s])