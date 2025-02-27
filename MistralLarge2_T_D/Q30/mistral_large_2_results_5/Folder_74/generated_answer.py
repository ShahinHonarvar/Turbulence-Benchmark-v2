def insert_before_character(s):
    return ' '.join([' ' + char if char == 'T' else char for char in s])