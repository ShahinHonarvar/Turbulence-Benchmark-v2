def insert_after_character(s):
    return ''.join([char + ('n' if char == 'H' else '') for char in s])