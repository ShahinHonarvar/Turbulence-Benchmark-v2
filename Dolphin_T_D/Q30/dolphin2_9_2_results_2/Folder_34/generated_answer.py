def insert_before_character(string):
    return ''.join(('a' + char if char == 'A' else char for char in string))