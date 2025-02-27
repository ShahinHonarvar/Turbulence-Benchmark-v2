def insert_after_character(string):
    return ' '.join([char + 'P' if char == ' ' else char for char in string])