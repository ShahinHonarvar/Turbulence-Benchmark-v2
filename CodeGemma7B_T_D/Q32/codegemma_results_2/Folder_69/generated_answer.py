def insert_after_character(text):
    new_text = ''
    for char in text:
        if char == ' ':
            new_text += char + 'P'
        else:
            new_text += char
    return new_text