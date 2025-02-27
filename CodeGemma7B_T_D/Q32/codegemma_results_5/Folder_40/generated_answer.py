def insert_after_character(string):
    """Inserts 'e' after each 'e' in a string."""
    result = ''
    for char in string:
        if char == 'e':
            result += 'e'
        result += char
    return result