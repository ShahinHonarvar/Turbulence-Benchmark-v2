def insert_after_character(text):
    modified_text = ''
    for char in text:
        if char == 'U':
            modified_text += char + 'T'
        else:
            modified_text += char
    return modified_text