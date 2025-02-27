def insert_before_character(string):
    return ' '.join((' ' if character == 'T' else character for character in string))