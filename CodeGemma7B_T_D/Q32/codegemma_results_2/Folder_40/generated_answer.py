def insert_after_character(text):
    new_text = ''
    for char in text:
        new_text += char
        if char == 'e':
            new_text += 'e'
    return new_text