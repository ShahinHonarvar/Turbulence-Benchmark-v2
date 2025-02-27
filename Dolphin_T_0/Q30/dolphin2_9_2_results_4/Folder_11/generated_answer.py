def insert_before_character(string):
    return ''.join(('t' + char if char == 'g' else char for char in string))