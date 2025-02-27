def insert_after_character(text):
    updated_text = []
    for char in text:
        if char == ' ':
            updated_text.append('H')
        updated_text.append(char)
    return ''.join(updated_text)