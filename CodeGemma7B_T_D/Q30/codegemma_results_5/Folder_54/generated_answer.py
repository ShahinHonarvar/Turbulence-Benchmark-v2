def insert_before_character(text):
    updated_text = ''
    for char in text:
        if char == 'M':
            updated_text += 'f' + char
        else:
            updated_text += char
    return updated_text