def insert_after_character(text):
    new_text = ''
    for char in text:
        if char == 'a':
            new_text += char + 'W'
        else:
            new_text += char
    return new_text