def insert_before_character(s):
    return ''.join(('Uu' if char == 'u' else char for char in s))