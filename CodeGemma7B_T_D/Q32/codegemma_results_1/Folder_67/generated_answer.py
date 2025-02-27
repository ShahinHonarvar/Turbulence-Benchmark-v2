def insert_after_character(text):
    updated_text = ''
    for char in text:
        updated_text += char
        if char == 'j':
            updated_text += '1'
    return updated_text