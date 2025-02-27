def insert_after_character(string):
    return ''.join([char + ('I' if char == 'I' else '') for char in string])