def insert_after_character(text):
    new_text = ''
    for i in text:
        new_text += i
        if i == 'O':
            new_text += 'o'
    return new_text