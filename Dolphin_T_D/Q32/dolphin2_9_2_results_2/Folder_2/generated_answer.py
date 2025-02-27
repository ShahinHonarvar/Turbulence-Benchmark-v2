def insert_after_character(mystring):
    return ''.join(('Z' if i == 'C' else c for i, c in mystring))