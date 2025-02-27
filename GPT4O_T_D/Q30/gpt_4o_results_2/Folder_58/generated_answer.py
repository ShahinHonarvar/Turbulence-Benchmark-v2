def insert_before_character(s):
    return ''.join(('oF' if char == 'F' else char for char in s))