def insert_before_character(text):
    for i in range(len(text)):
        if text[i] == 'c':
            text = text[:i] + 'G' + text[i:]
    return text