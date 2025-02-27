def insert_after_character(text):
    modified_text = ''
    for char in text:
        if char == 't':
            modified_text += char + 'G'
        else:
            modified_text += char
    return modified_text