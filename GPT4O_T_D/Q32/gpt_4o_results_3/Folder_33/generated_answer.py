def insert_after_character(string):
    return ''.join(('a' + 'n' if char == 'a' else char for char in string))