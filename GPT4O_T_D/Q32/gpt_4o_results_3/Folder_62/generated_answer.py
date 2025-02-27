def insert_after_character(s):
    return ''.join((x + 'o' if x == ' ' else x for x in s))