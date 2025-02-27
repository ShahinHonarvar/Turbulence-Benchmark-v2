def insert_before_character(string):
    return ''.join((c + 'W' if c == ' ' else c for c in string))