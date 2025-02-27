def insert_after_character(s):
    return ''.join((char + 'm' if char == 'F' else char for char in s))