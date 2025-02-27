def insert_before_character(text):
    new_text = ''
    for char in text:
        if char == 'g':
            new_text += 'M' + char
        else:
            new_text += char
    return new_text