def insert_before_character(s):
    return ''.join(('N' + char if char == 'B' else char for char in s))