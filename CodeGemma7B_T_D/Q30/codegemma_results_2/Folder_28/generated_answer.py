def insert_before_character(string):
    return ''.join((c + '1' if c == 'r' else c for c in string))