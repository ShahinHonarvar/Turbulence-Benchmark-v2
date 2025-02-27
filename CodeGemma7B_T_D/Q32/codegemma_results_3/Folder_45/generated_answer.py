def insert_after_character(text):
    text = text.replace('O', 'O+')
    text = text.replace('+', 'O')
    return text