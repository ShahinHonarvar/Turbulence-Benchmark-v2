def insert_after_character(text):
    """Inserts 't' after every 'g' in a string."""
    new_text = ''
    for char in text:
        if char == 'g':
            new_text += 'gt'
        else:
            new_text += char
    return new_text