def insert_before_character(s):
    return ''.join(('v' + char if char == 'j' else char for char in s))