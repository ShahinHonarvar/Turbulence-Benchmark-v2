def insert_after_character(str):
    return ''.join([c + 'H' if c == '0' else c for c in str])