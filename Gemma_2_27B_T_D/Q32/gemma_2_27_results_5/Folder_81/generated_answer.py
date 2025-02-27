def insert_after_character(text):
    new_text = ''
    for char in text:
        new_text += char
        if char == 'A':
            new_text += 'A'
    return new_text