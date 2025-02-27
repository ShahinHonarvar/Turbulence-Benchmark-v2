def insert_before_character(str):
    return ''.join((char + 'e' if char == 'E' else char for char in str))