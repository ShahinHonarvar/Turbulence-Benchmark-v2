def insert_before_character(string):
    """Inserts 'd' before each 'O' in a string."""
    return ''.join((char + ('d' if char == 'O' else '') for char in string))