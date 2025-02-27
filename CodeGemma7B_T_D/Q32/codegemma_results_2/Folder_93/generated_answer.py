def insert_after_character(text):
    new_text = ''
    for i in range(len(text)):
        if text[i] == 'Y':
            new_text += text[i] + '4'
        else:
            new_text += text[i]
    return new_text