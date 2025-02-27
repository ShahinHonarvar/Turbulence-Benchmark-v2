def insert_after_character(string):
    return ''.join(['C' + 'H' + c if c == 'C' else c for c in string])