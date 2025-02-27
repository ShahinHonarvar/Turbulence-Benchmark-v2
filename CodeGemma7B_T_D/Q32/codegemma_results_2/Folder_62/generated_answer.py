def insert_after_character(text):
    """Inserts 'o' after each space in a string."""
    output = ''
    for character in text:
        if character == ' ':
            output += character + 'o'
        else:
            output += character
    return output