def insert_after_character(s):
    return ''.join(('II' if char == 'I' else char for char in s))