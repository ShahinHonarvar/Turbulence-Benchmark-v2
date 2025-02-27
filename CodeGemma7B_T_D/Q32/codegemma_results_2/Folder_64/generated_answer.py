def insert_after_character(text):
    new_text = ''
    for char in text:
        if char == 'u':
            new_text += char + 'u'
        else:
            new_text += char
    return new_text