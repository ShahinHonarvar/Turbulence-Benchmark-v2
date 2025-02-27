def insert_after_character(text):
    new_text = []
    for char in text:
        if char == 'O':
            new_text.append(char)
            new_text.append('O')
        else:
            new_text.append(char)
    return ''.join(new_text)