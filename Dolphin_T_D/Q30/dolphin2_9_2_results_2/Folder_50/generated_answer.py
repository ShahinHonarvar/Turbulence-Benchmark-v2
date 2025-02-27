def insert_before_character(string):
    return 'u'.join(('t' if char == 't' else str(char) for char in string))