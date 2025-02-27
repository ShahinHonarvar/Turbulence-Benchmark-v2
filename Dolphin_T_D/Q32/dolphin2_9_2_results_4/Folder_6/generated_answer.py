def insert_after_character(text):
    new_text = ''
    for char in text:
        new_text += char
        if char == 'X':
            new_text += 'u'
    return new_text