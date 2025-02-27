def insert_before_character(s):
    return ''.join(('H' + char if char == 'A' else char for char in s))