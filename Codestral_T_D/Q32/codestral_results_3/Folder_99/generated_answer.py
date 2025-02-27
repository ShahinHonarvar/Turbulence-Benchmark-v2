def insert_after_character(string):
    return ''.join(('W' + char if char == 'a' else char for char in string))