def insert_before_character(text):
    new_text = ''
    for char in text:
        if char == 'r':
            new_text += 'w' + char
        else:
            new_text += char
    return new_text