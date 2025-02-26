def insert_before_character(s):
    return ''.join(['G' + char if char == 'c' else char for char in s])