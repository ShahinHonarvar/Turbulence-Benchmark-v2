def insert_before_character(s):
    return ''.join(('j' + char if char == 'N' else char for char in s))