def insert_before_character(s):
    return ''.join(('0' + char if char == 'e' else char for char in s))