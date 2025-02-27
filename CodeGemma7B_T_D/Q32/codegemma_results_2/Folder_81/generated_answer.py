def insert_after_character(text):
    new_text = ''
    for char in text:
        if char == 'A':
            new_text += char + 'A'
        else:
            new_text += char
    return new_text