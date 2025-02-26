def insert_before_character(string):
    return ''.join(['G' + char if char == 't' else char for char in string])