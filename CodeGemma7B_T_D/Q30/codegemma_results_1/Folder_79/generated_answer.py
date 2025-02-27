def insert_before_character(text):
    for i in range(len(text)):
        if text[i] == 'E':
            text = text[:i] + 'E' + text[i:]
    return text