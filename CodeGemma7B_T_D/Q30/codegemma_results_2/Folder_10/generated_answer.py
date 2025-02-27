def insert_before_character(text):
    updated_text = ''
    for char in text:
        if char == 'j':
            updated_text += 'v' + char
        else:
            updated_text += char
    return updated_text