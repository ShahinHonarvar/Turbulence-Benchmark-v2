def insert_before_character(s):
    return ''.join(('M' + char if char == 'g' else char for char in s))