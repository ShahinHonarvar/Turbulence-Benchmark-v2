def insert_after_character(text):
    updated_text = ''
    for char in text:
        if char == 'i':
            updated_text += char + '0'
        else:
            updated_text += char
    return updated_text