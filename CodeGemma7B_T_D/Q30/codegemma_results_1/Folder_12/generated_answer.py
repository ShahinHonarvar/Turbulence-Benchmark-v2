def insert_before_character(text):
    while 'I' in text:
        index = text.find('I')
        text = text[:index] + ' ' + text[index:]
    return text