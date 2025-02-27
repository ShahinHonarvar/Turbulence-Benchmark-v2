def insert_after_character(s):
    return ''.join([char + '0' if char == 'e' else char for char in s])