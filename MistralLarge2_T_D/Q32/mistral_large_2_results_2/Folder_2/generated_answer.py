def insert_after_character(s):
    return ''.join([char + ('Z' if char == 'C' else '') for char in s])