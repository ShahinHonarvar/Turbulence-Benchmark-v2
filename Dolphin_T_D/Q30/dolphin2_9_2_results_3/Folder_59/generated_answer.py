def insert_before_character(text):
    if text.count('o') == 0:
        return text
    new_text = ''
    for char in text:
        if char == 'o':
            new_text += '0' + char
        else:
            new_text += char
    return new_text