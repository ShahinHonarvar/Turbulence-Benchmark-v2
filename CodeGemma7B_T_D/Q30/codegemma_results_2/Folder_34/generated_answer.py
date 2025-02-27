def insert_before_character(text):
    if not text:
        return text
    new_text = []
    for char in text:
        if char == 'A':
            new_text.append('a')
        new_text.append(char)
    return ''.join(new_text)