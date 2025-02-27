def insert_before_character(string):
    return 'q'.join(('U' if char == 'U' else str(char) for char in string))