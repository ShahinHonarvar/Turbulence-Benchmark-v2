def insert_before_character(txt):
    return ''.join([char if char != 'O' else char + 'o' for char in txt])