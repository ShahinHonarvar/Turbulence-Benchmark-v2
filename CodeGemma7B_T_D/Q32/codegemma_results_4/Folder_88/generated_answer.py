def insert_after_character(text):
    """
            Inserts 't' immediately succeeding any occurrences of 'a' in a string.
            """
    new_text = ''
    for char in text:
        if char == 'a':
            new_text += char + 't'
        else:
            new_text += char
    return new_text