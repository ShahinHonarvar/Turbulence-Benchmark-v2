def insert_before_character(s):
    return ''.join((('w' if char == 's' else '') + char for char in s))