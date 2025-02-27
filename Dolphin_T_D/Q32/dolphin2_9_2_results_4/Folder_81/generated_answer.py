def insert_after_character(string):
    return ''.join([char + 'A' if char == 'A' else char for char in string])