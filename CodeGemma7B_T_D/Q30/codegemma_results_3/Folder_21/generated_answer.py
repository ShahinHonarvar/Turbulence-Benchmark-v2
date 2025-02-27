def insert_before_character(text):
    """Inserts the letter 'K' before any spaces in a string."""
    k_inserted_text = ''
    for char in text:
        if char == ' ':
            k_inserted_text += 'K' + char
        else:
            k_inserted_text += char
    return k_inserted_text