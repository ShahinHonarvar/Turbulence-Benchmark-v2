def insert_before_character(str):
    return ''.join((char + ('Q' if char == 'm' else '') for char in str))