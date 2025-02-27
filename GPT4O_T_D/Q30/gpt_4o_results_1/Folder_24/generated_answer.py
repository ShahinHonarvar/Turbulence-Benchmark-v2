def insert_before_character(s):
    return ''.join(('4' + char if char == '0' else char for char in s))