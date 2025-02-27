def insert_after_character(s):
    return ''.join((char + ('u' if char == 't' else '') for char in s))