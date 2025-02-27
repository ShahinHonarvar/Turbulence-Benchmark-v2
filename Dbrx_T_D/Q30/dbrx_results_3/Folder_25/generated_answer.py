def insert_before_character(string):
    return ''.join(['W' + char if char == 'e' else char for char in string])