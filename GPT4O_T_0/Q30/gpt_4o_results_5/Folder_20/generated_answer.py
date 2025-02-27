def insert_before_character(s):
    return ''.join(('H' + char if char == 'C' else char for char in s))