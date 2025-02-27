def insert_after_character(text):
    for i, char in enumerate(text):
        if char == 'U':
            text = text[:i + 1] + 'a' + text[i + 1:]
    return text