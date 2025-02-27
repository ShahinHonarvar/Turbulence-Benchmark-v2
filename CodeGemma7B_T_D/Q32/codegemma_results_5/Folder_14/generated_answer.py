def insert_after_character(text):
    text = text.split()
    text = [' ' + word for word in text]
    text = ' '.join(text)
    return text