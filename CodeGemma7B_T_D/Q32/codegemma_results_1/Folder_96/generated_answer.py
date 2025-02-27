def insert_after_character(string):
    return ''.join([char + ('A' if char == 'a' else '') for char in string])