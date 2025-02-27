def insert_before_character(s):
    return ''.join(('V' + char if char == 'P' else char for char in s))