def insert_before_character(s):
    return 'H' + ''.join(('H' if c == ' ' else c for c in s))