def insert_before_character(s):
    return ''.join(('mF' if char == 'F' else char for char in s))