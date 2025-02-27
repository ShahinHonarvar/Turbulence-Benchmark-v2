def insert_before_character(string):
    return ''.join((char + '0' if char == 'a' else char for char in string))