def insert_after_character(s):
    return ''.join([char + ('E' if char == 'E' else '') for char in s])