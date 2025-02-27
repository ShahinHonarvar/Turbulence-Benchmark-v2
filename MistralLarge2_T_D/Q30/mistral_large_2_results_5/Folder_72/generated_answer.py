def insert_before_character(string):
    return ''.join(['d' + char if char == 'O' else char for char in string])