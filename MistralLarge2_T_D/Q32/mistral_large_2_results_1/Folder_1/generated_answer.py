def insert_after_character(s):
    return ''.join((char + ('T' if char == 'U' else '') for char in s))