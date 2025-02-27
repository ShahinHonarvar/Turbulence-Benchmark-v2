def insert_after_character(s):
    return ''.join([char + ('o' if char == 'O' else '') for char in s])