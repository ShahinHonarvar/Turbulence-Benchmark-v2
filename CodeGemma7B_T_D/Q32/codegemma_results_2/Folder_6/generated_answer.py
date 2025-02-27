def insert_after_character(text):
    text_split = text.split('X')
    new_text = ''
    for substring in text_split:
        new_text += substring + 'u'
    return new_text