def insert_before_character(str):
    return ''.join([c + '0' if c == 'a' else c for c in str])