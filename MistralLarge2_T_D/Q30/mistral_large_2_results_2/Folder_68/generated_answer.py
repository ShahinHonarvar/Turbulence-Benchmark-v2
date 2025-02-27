def insert_before_character(s):
    return ''.join(['0' + char if char == 'i' else char for char in s])