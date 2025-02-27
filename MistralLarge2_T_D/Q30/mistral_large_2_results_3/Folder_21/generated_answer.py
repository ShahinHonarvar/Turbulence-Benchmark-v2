def insert_before_character(string):
    return ''.join(('K' + char if char == ' ' else char for char in string))