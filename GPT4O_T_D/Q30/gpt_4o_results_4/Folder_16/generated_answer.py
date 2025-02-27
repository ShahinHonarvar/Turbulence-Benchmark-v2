def insert_before_character(s):
    return ''.join(['n' + char if char == 'w' else char for char in s])