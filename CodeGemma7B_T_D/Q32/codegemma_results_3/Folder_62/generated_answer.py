def insert_after_character(text):
    return ' '.join([word + 'o' if ' ' in word else word for word in text.split()])