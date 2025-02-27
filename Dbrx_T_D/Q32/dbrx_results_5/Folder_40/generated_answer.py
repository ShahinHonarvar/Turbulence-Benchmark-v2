def insert_after_character(string):
    return ''.join((char if char != 'e' else 'ee' for char in string))