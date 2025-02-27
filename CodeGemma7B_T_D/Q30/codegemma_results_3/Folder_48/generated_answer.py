def insert_before_character(text):
    new_text = ''
    for char in text:
        if char == 'S':
            new_text += 'U' + char
        else:
            new_text += char
    return new_text