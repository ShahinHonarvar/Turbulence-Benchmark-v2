def insert_before_character(text):
    """Inserts 'u' before all occurrences of 'X' in a string."""
    new_text = ''
    for char in text:
        if char == 'X':
            new_text += 'u' + char
        else:
            new_text += char
    return new_text