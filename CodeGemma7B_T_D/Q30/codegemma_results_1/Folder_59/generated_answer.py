def insert_before_character(text):
    for i, char in enumerate(text):
        if char == 'o':
            text = text[:i] + '0' + text[i:]
    return text