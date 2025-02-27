def insert_after_character(text):
    for i in range(len(text)):
        if text[i] == 'k':
            text = text[:i + 1] + 'k' + text[i + 1:]
    return text