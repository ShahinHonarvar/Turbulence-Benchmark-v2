def insert_after_character(s):
    return ''.join((char + 'n' if char == 'a' else char for char in s))