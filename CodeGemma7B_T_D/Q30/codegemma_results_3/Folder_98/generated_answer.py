def insert_before_character(text):
    new_text = ''
    for i in range(len(text)):
        if text[i] == 'U':
            new_text += text[i - 1]
        new_text += text[i]
    return new_text