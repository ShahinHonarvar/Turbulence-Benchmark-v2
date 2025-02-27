def insert_before_character(text):
    new_text = ''
    for char in text:
        if char == ' ':
            new_text += 'H '
        else:
            new_text += char
    return new_text