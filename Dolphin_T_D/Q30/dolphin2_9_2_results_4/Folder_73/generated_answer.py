def insert_before_character(string):
    return ''.join(('V' if character == 'R' else character for character in string))