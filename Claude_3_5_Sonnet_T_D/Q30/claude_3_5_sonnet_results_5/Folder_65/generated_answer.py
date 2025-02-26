def insert_before_character(s):
    return ''.join(['9' + char if char == '6' else char for char in s])