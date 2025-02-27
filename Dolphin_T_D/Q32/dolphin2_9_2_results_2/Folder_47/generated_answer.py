def insert_after_character(s):
    return ''.join((f'{char}f' if char == 'E' else char for char in s))