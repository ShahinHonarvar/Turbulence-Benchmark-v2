def insert_after_character(s):
    return ''.join(('H' + c if c == 'C' else c for c in s))