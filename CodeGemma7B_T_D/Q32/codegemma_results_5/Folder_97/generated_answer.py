def insert_after_character(s):
    return ''.join([char + 'h' if char == 'o' else char for char in s])