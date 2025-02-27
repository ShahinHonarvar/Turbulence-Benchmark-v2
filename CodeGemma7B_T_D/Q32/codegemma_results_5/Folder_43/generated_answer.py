def insert_after_character(text):
    new_text = ''
    for char in text:
        if char == 't':
            new_text += char + 'G'
        else:
            new_text += char
    return new_text