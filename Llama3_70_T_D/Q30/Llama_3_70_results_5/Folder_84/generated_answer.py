def insert_before_character(s):
    return ''.join(('n' + c if c == 'H' else c for c in s))