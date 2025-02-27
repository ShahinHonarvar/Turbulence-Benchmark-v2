def insert_after_character(s):
    return ''.join(['H' + c if c == '0' else c for c in s])