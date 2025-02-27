def insert_before_character(string):
    return ''.join(('P' if character == 'C' else character for character in string))