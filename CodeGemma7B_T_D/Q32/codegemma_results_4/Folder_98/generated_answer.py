def insert_after_character(text):
    new_text = ''
    for char in text:
        if char == 'U':
            new_text += 'u'
        new_text += char
    return new_text