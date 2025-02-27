def insert_after_character(s):
    return ''.join([char + 'o' if char == 'o' else char for char in s])