def insert_before_character(s):
    return ''.join(('V' + char if char == 'R' else char for char in s))