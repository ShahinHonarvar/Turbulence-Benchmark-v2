def insert_before_character(string):
    return ''.join((c + ' ' if c == ' ' else c for c in string))