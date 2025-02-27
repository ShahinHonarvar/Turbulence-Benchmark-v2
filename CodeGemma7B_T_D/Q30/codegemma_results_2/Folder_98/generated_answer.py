def insert_before_character(text):
    new_text = []
    for char in text:
        if char == 'U':
            new_text.append('u')
            new_text.append('U')
        else:
            new_text.append(char)
    return ''.join(new_text)