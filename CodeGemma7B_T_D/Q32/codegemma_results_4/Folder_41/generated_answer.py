def insert_after_character(text):
    replaced_text = ''
    for char in text:
        if char == 'O':
            replaced_text += char + 'o'
        else:
            replaced_text += char
    return replaced_text