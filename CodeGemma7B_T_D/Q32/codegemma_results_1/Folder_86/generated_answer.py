def insert_after_character(text):
    new_text = ''
    for i in range(len(text)):
        if text[i] == 'O':
            new_text += text[i] + 'Q'
        else:
            new_text += text[i]
    return new_text