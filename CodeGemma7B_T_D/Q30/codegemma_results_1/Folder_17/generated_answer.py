def insert_before_character(text):
    new_text = ''
    for char in text:
        if char == 'Q':
            new_text += 'I' + char
        else:
            new_text += char
    return new_text