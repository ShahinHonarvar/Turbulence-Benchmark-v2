def insert_before_character(str):
    return ''.join((c + ' ' if c == ' ' else c for c in str))