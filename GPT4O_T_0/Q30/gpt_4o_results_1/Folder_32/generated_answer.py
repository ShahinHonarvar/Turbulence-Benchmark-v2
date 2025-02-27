def insert_before_character(s):
    return ''.join(('uF' if char == 'F' else char for char in s))