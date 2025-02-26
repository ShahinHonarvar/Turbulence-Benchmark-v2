def insert_before_character(string):
    return ''.join(['1' + char if char == 'r' else char for char in string])