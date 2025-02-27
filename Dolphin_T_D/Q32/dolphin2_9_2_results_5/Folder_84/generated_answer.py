def insert_after_character(s):
    return ''.join(['H' + n + c if c == 'H' else c for c in s]) + n