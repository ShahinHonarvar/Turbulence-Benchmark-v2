def insert_before_character(string):
    return ''.join(['I' + char if char == 'Q' else char for char in string])