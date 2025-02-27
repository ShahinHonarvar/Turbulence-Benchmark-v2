def insert_after_character(string):
    return ''.join((char + ('q' if char == 'U' else '') for char in string))