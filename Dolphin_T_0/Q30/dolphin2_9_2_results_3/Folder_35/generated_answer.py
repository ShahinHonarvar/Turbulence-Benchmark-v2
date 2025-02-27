def insert_before_character(string):
    return 'M'.join(('9' if char == '9' else str(char) for char in string))