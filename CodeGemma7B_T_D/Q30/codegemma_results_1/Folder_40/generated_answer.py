def insert_before_character(text):
    new_text = []
    for char in text:
        if char == 'e':
            new_text.append('e')
        new_text.append(char)
    return ''.join(new_text)