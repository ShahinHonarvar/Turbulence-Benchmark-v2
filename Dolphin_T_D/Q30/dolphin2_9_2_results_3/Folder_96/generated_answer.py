def insert_before_character(string):
    return ''.join(('A' + character if character == 'a' else character for character in string))