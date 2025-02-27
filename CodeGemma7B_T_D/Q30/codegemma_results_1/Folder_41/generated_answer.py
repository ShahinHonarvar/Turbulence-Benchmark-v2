def insert_before_character(string):
    return ''.join([character if character != 'O' else 'o' + character for character in string])