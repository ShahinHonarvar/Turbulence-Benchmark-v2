def insert_before_character(string):
    return ''.join([char + 'T' if char == 'U' else char for char in string])