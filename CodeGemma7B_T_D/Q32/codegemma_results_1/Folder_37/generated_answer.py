def insert_after_character(text):
    for i in range(len(text)):
        if text[i] == 'U':
            text = text[:i + 1] + 'a' + text[i + 1:]
    return text