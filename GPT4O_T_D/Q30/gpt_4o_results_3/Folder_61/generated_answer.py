def insert_before_character(string):
    return ''.join(('0e' if char == 'e' else char for char in string))