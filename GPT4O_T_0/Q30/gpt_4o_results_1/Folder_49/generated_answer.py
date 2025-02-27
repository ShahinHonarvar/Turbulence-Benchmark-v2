def insert_before_character(s):
    return ''.join(('i' + char if char == 'i' else char for char in s))