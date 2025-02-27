def insert_before_character(str):
    return ''.join([c if c != 'e' else 'E' + c for c in str])