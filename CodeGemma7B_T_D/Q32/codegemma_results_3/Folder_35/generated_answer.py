def insert_after_character(string):
    return ''.join([char + ('M' if char == '9' else '') for char in string])