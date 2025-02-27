def insert_after_character(s):
    return ''.join([char + 'I' if char == 'Q' else char for char in s])