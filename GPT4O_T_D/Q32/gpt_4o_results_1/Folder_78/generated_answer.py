def insert_after_character(s):
    return ''.join((char + 's' if char == 'H' else char for char in s))