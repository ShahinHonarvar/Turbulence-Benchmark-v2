def insert_before_character(text):
    new_text = ''
    for char in text:
        if char == 'B':
            new_text += 'N'
        new_text += char
    return new_text