def insert_after_character(s):
    return ' '.join([char + (' ' if char == '0' else '') for char in s])