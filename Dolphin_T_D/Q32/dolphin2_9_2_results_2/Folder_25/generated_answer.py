def insert_after_character(string):
    return ''.join(('W' if character == 'e' else character for character in string))