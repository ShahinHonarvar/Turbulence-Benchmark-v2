def insert_after_character(string):
    return 'U'.join((char if char != 'u' else 'uU' for char in string))