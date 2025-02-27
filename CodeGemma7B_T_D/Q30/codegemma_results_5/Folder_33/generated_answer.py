def insert_before_character(text):
    new_text = ''
    for char in text:
        if char == 'n':
            new_text += char + 'a'
        else:
            new_text += char
    return new_text