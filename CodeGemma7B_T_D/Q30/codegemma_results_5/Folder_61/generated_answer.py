def insert_before_character(string):
    return ''.join([char if char != 'e' else '0e' for char in string])