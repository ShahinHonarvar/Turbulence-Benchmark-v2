def insert_before_character(str):
    return ''.join((x + 'H' if x == ' ' else x for x in str))