def insert_after_character(text):
    """Inserts 'a' after each occurrence of 'A' in a string."""
    new_text = ''
    for char in text:
        if char == 'A':
            new_text += char + 'a'
        else:
            new_text += char
    return new_text