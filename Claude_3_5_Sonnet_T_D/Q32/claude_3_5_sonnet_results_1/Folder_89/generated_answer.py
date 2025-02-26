def insert_after_character(string):
    return ''.join([char + 'W' if char == ' ' else char for char in string])