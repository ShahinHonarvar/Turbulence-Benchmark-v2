def insert_after_character(text):
    new_text = ''
    for char in text:
        if char == 'k' or (new_text != '' and new_text[-1] == 'k'):
            new_text += char + 'k'
        else:
            new_text += char
    return new_text