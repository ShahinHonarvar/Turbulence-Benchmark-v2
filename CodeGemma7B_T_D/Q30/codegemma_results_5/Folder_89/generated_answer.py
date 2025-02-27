def insert_before_character(text):
    return ''.join([char + 'W' if char == ' ' and i != 0 else char for i, char in enumerate(text)])