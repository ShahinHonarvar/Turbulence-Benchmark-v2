def insert_before_character(text):
    for i in range(len(text)):
        if text[i] == 'U':
            return text[:i] + 'q' + text[i:]
    return text