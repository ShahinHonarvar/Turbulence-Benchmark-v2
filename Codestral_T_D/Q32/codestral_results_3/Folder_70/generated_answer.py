def insert_after_character(string):
    return ''.join(('PV' if char == 'P' else char for char in string))