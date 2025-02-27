def insert_before_character(string):
    return ''.join(['H' if i == 'A' else c for i, c in string]) + 'H'