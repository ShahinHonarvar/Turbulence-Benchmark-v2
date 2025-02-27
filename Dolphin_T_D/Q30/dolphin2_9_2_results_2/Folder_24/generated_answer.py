def insert_before_character(string):
    return '4'.join(('0' if character == '0' else str(character) for character in string))