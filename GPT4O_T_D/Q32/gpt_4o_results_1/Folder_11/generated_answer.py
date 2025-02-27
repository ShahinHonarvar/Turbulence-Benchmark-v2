def insert_after_character(s):
    return ''.join([char + 't' if char == 'g' else char for char in s])