def insert_before_character(string):
    return ''.join((char + ('a' if char == 'U' else '') for char in string))