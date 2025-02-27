def insert_after_character(text):
    new_text = ''
    for char in text:
        if char == 'm':
            new_text += char + 'N'
        else:
            new_text += char
    return new_text