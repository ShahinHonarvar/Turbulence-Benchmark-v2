def insert_before_character(string):
    return ''.join(('n' + char if char == 'H' else char for char in string))