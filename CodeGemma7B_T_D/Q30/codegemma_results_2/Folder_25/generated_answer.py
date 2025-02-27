def insert_before_character(text):
    """Inserts character 'W' before all occurrences of character 'e' in a string."""
    new_text = ''
    for char in text:
        if char == 'e':
            new_text += 'W' + char
        else:
            new_text += char
    return new_text