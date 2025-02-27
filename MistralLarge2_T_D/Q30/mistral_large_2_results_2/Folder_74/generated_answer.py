def insert_before_character(s):
    return ' '.join([char if char != 'T' else ' T' for char in s])