def insert_before_character(s):
    return ''.join(['f' + char if char == 'M' else char for char in s])