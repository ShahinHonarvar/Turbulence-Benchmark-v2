def insert_before_character(s):
    return ''.join(['q' + char if char == 'j' else char for char in s])