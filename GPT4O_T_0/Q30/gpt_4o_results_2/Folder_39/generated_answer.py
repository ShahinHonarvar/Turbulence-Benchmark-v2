def insert_before_character(s):
    return ''.join(('Qm' if char == 'm' else char for char in s))