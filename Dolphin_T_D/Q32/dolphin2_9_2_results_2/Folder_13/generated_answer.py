def insert_after_character(text):
    new_text = ''
    for i in range(len(text)):
        new_text += text[i]
        if text[i] == 'x':
            new_text += 'N'
    return new_text