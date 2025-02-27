def insert_after_character(text):
    for i, char in enumerate(text):
        if char == 'O':
            text = text[:i + 1] + 'j' + text[i + 1:]
    return text