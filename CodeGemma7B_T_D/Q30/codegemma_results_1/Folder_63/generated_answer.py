def insert_before_character(text):
    for i in range(len(text)):
        if text[i] == '5':
            text = text[:i] + 'R' + text[i:]
    return text