def insert_after_character(string):
    return ' '.join(('0 ' + char if char == '0' else char for char in string))