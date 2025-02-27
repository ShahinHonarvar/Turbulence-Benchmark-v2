def insert_before_character(str):
    text = str
    for i in range(len(text)):
        if text[i] == 'K':
            text = text[:i] + 'l' + text[i:]
    return text