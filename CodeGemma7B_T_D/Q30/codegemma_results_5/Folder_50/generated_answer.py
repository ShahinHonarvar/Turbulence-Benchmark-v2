def insert_before_character(string):
    return ''.join((char + 'u' if char == 't' else char for char in string))