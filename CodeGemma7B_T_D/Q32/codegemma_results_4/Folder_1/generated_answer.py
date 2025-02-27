def insert_after_character(text):
    new_text = text
    for char in text:
        if char == 'U':
            index = new_text.index(char)
            new_text = new_text[:index + 1] + 'T' + new_text[index + 1:]
    return new_text