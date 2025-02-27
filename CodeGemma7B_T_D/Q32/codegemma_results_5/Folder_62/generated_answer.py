def insert_after_character(text):
    """Insert character 'o' after every space character in the input string."""
    new_text = ''
    for char in text:
        if char == ' ':
            new_text += char + 'o'
        else:
            new_text += char
    return new_text