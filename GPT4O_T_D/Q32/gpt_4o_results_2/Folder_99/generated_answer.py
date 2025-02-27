def insert_after_character(s):
    return ''.join([char + ('W' if char == 'a' else '') for char in s])