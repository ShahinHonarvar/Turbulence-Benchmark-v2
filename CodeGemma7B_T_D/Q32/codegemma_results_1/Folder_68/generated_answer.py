def insert_after_character(text):
    for i in range(len(text)):
        if text[i] == 'i':
            text = text[:i + 1] + '0' + text[i + 1:]
    return text