def insert_after_character(string):
    return ''.join(['e' + c if c == 'E' else c for c in string])