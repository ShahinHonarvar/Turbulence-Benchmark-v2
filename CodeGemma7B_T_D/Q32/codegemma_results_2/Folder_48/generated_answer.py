def insert_after_character(string):
    return ''.join([char + 'U' if char == 'S' else char for char in string])