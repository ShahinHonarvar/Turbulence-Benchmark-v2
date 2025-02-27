def insert_before_character(s):
    return ''.join(['H' + c if c == 'A' else c for c in s])