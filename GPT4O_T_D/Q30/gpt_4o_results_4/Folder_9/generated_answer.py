def insert_before_character(s):
    return ''.join(('Ee' if char == 'e' else char for char in s))