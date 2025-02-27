def insert_before_character(s):
    return ''.join(['S' + char if char == '2' else char for char in s])