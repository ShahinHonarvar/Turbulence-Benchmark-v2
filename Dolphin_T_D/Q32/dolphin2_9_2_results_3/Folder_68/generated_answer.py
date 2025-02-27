def insert_after_character(string):
    return ''.join([char + '0' if char == 'i' else char for char in string])