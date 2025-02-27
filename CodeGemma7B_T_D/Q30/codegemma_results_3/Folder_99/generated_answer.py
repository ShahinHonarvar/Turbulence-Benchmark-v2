def insert_before_character(string):
    return ''.join([char + ('W' if char == 'a' else '') for char in string])